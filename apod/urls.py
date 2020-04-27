from django.urls import path
from apod import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import include

router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'images', views.ImageViewSet)
# router.register(r'users', UserViewSet)

# author_list = AuthorViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
#
# author_detail = AuthorViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
#
# image_list = ImageViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
#
# image_detail = ImageViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
#
#
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

urlpatterns = [
    # path('apod/authors/', author_list, name='author-list'),
    # path('apod/author/<int:pk>/', author_detail, name='author-detail'),
    # path('apod/images/', image_list, name='image-list'),
    # path('apod/image/<int:pk>/', image_detail, name='image-detail'),
    # path('users/', user_list, name='user-list'),
    # path('user/<int:pk>/', user_detail, name='user-detail'),
    # path('', api_root),
    # path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('extract/', views.extract),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

#from rest_framework.urlpatterns import  format_suffix_patterns
#from apod import views

#urlpatterns = [
#    path('apod/authors/', views.author_list),
#    path('apod/author/<int:pk>/', views.author_detail),
#    path('apod/images/', views.image_list),
#    path('apod/image/<int:pk>/', views.image_detail),
#]

#urlpatterns = format_suffix_patterns(urlpatterns)

