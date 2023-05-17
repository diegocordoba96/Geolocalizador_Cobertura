from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from app.views import Login, Registro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('', include('Planes.urls')),
    path('generar_token/',views.obtain_auth_token),
    path('login/',Login.as_view(), name= 'login'),
    path('registro/',Registro.as_view(), name= 'registro'),

]
