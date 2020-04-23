from django.urls import path
from apod import views

urlpatterns = [
    path('apod/authors/', views.author_list),
    path('apod/authors/<int:pk>/', views.author_detail),
]
