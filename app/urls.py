from django.urls import path
from general.api import  get_cobertura, get_planes

urlpatterns = [
    path('cobertura/' ,get_cobertura, name ='cobertura'),
]