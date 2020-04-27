from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import  Http404
from apod.models import Author
from apod.serializers import AuthorSerializers


class AuthorList(APIView):

    def get(self, request, format=None):
        authors = Author.objects.all()
        serializer = AuthorSerializers(authors, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthorSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetail(APIView):

    def get_object(self,pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        author = self.get_object(pk)
        serializer = AuthorSerializers(author)
# @csrf_exempt
# def author_list(request):
#     if request.method == 'GET':
#         authors = Author.objects.all()
#         serializer = AuthorSerializers(authors, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     if request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = AuthorSerializers(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
# @csrf_exempt
# def author_detail(request, pk):
#     try:
#         author = Author.objects.get(pk=pk)
#     except Author.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = AuthorSerializers(author)
#         return JsonResponse(serializer.data)
#
#     if request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = AuthorSerializers(author, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     if request.method == 'DELETE':
#         author.delete()
#         return HttpResponse(status=204)
