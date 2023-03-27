"""Tercero_C_jojsanchezz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from inicioApp import views
from inicioApp.views import formularioafiview
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.inicioDef,name='inicio'),
    path('', views.mantenDef,name='mantemiento'),
    path('admin/', admin.site.urls),
    #path('registro/',views.registro, name='registroprueba'),
    path('registrarusuario/', formularioafiview.index, name='registrouser'),
    path('guardarusuario/', formularioafiview.procesar_formulario, name='guardarusuario'),
    path('listarusuario/', formularioafiview.listar_usuario, name='listarusuario'),
    path('editarusuario/<id_usuario>/',formularioafiview.edit, name='editarusuario'),
    path('actualizarusuario/<id_usuario>/',formularioafiview.actualizar_usuario, name='actualizarusuario'),
    path('eliminarausuario/<id_usuario>/',formularioafiview.delete, name='eliminarusuario'),
    path('accounts/',include('django.contrib.auth.urls')),

]
