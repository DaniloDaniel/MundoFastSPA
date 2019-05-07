from django.urls import path

from . import views

app_name = 'MundoFastWebApp'
urlpatterns = [
    # ex: /MundoFastWebApp/
    path('', views.index, name='index'),
    # ex: /MundoFastWebApp/usuarios/
    path('usuarios/', views.usuarios, name='usuarios'),
    # ex: /MundoFastWebApp/usuarios/1/
    path('usuarios/<int:id>/', views.verUsuario, name='verUsuario'),
    # ex: /MundoFastWebApp/usuarios/crearUsuario/
    path('usuarios/crearUsuario/', views.crearUsuario, name='crearUsuario'),
    # Registro en: /MundoFastWebApp/usuarios/crearUsuario/
    path('usuarios/formUsuario/', views.formUsuario, name='formUsuario'),
]