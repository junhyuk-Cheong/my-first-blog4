from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('map', views.map, name='map'),
    path('index', views.index, name='index'),
]

