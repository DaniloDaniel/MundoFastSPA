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
    # Registro: /MundoFastWebApp/usuarios/crearUsuario/
    path('usuarios/formUsuario/', views.formUsuario, name='formUsuario'),
    # Modificar: /MundoFastWebApp/usuarios/modificarUsuario/1/
    path('usuarios/modificarUsuario/<int:id>/', views.modificarUsuario, name='modificarUsuario'),
    # Eliminar: /MundoFastWebApp/usuarios/eliminarUsuario/1/
    path('usuarios/eliminarUsuario/<int:id>/', views.eliminarUsuario, name='eliminarUsuario'),
    path('productos/', views.productos, name='productos'),
    path('productos/crearproducto/', views.crearProducto, name='crearproducto'),
    path('productos/<int:id>/', views.verProducto, name='verproducto'),
    path('productos/formproducto/', views.formProducto, name='formproducto'),
    path('productos/modificar/<int:id>/', views.modificarProducto, name='modificarproducto'),
    path('productos/eliminar/<int:id>/', views.eliminarProducto, name='eliminarproducto'),
    path('productos/ofertas/', views.ofertaProducto, name='ofertaproducto'),
    path('productos/buscar/', views.buscarProducto, name='buscarproducto'),
]