from django.urls import path
from general.api import  get_cobertura, get_planes

urlpatterns = [
    path('planes/' ,get_planes, name ='planes'),
]