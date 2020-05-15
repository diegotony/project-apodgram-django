from django.urls import path
from apod import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import include

router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'images', views.ImageViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('extract/', views.extract , name="extract-apod-data"),
    path('like/<int:id>/', views.like , name="like-image"),

]
