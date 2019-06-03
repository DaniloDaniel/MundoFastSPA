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
    # Buscar: /MundoFastWebApp/usuarios/buscarUsuario/1/
    path('usuarios/buscarUsuario/', views.buscarUsuario, name='buscarUsuario'),
    # Productos:
    path('productos/', views.productos, name='productos'),
    path('productos/crearproducto/', views.crearProducto, name='crearproducto'),
    path('productos/<int:id>/', views.verProducto, name='verproducto'),
    path('productos/formproducto/', views.formProducto, name='formproducto'),
    path('productos/modificar/<int:id>/', views.modificarProducto, name='modificarproducto'),
    path('productos/eliminar/<int:id>/', views.eliminarProducto, name='eliminarproducto'),
    path('productos/ofertas/', views.ofertaProducto, name='ofertaproducto'),
    path('productos/buscar/', views.buscarProducto, name='buscarproducto'),
    # Ventas:
    path('ventas/', views.ventas, name='ventas'),
    path('ventas/formVenta/', views.formVenta, name='formVenta'),
    path('ventas/crearVenta/', views.crearVenta, name='crearVenta'),
    path('ventas/buscar/', views.buscarVenta, name='buscarVenta'),
    path('ventas/<int:id>/', views.verVenta, name='verVenta'),
    path('ventas/modificar/<int:id>/', views.modificarVenta, name='modificarVenta'),
    path('ventas/eliminar/<int:id>/', views.eliminarVenta, name='eliminarVenta'),
]