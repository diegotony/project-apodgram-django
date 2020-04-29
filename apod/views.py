from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, status
from apod.models import Author, Image
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

                        pass
                        author_serializer = AuthorSerializer(data=author)

                return Response(data, status=status.HTTP_200_OK)
            else:
                attempt_num += 1
                time.sleep(5)
        return Response({"status": False, 'msg': "Request Failed"}, status=r.status_code)
    else:
        return Response({'status': False, 'msg': 'Method not allowed'}, status=status.HTTP_404_NOT_FOUND)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# class AuthorList(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#
# class AuthorDetail(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

# class ImageList(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class ImageDetail(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer


# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
