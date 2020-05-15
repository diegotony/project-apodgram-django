from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from apod.models import Author, Image
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from apod.serializers import AuthorSerializer, ImageSerializer
import requests
import os
import time
import datetime

# UserSerializer
MAX_RETRIES = 5


@api_view(['GET'])
def extract(request, format=None):
    if request.method == 'GET':
        attempt_num = 0
        while attempt_num < MAX_RETRIES:
            api_url = os.environ.get('API_URL')
            api_key = os.environ.get('API_KEY')
            api_count = os.environ.get('API_COUNT')
            r = requests.get(api_url + "api_key=" + api_key + "&count=" + str(api_count), timeout=20)
            if r.status_code == 200:
                data = r.json()
                for i in data:
                    date_format = datetime.datetime.strptime(i['date'], '%Y-%m-%d')
                    if 'copyright' not in i.keys():
                        
                        image = i
                        image['copyright'] = 1
                        image['date'] = date_format
                        serializer = ImageSerializer(data=image)

                        if serializer.is_valid():
                            serializer.save()
                        else:
                            print(serializer.errors)
                    else:
                        author, created = Author.objects.get_or_create(name=i['copyright'])
                        image = i
                        if created:
                            image['copyright'] = author.id
                            image['date'] = date_format
                            serializer = ImageSerializer(data=image)
                            if serializer.is_valid():
                                serializer.save()
                            else:
                                print(serializer.errors)
                        else:
                            image['copyright'] = author.id
                            image['date'] = date_format
                            serializer = ImageSerializer(data=image)
                            if serializer.is_valid():
                                serializer.save()
                            else:
                                print(serializer.errors)

                        author_serializer = AuthorSerializer(data=author)

                return Response(data, status=status.HTTP_200_OK)
            else:
                attempt_num += 1
                time.sleep(5)
        return Response({"status": False, 'msg': "Request Failed"}, status=r.status_code)
    else:
        return Response({'status': False, 'msg': 'Method not allowed'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def like(request, id):
    if request.method == 'GET':
        image = get_object_or_404(Image, pk=id)
        print(image)
        data = {"like": image.like + int(1)}
        serializer = ImageSerializer(image,data=data,partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response({'status':True, 'data':serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class ImageResultSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 5000

    


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    pagination_class = ImageResultSetPagination
    
