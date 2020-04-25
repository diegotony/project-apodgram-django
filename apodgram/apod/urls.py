from django.urls import path
from rest_framework.urlpatterns import  format_suffix_patterns
from apod import views

urlpatterns = [
    path('apod/authors/', views.author_list),
    path('apod/author/<int:pk>/', views.author_detail),
    path('apod/images/', views.image_list),
    path('apod/image/<int:pk>/', views.image_detail),

]

urlpatterns = format_suffix_patterns(urlpatterns)
