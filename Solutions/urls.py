"""Solutions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls'), name = 'publicar'),
    path('', include('inicio.urls'), name = 'propuesta'),
    path('', include('inicio.urls'), name = 'registrar_cliente'),
    path('', include('inicio.urls'), name = 'registrar_trabajador'),
    path('', include('inicio.urls'), name = 'inicio'),
    path('', include('inicio.urls'), name= 'nosotros'),
    path('', include('inicio.urls'), name= 'anuncios'),
    path('', include('inicio.urls'), name= 'login'),
    path('', include('inicio.urls'), name= 'logout'),
    ]

admin.site.site_header = 'Administración de Solutions!'
admin.site.index_title = "Módulos de Administración"
admin.site.site_title = 'Solutions!'
