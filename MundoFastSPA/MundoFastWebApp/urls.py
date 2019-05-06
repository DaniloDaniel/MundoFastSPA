from django.urls import path

from . import views

app_name = 'MundoFastWebApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('productos/', views.productos, name='productos'),
    path('productos/crearproducto/', views.crearProducto, name='crearproducto'),
    path('productos/<int:id>/', views.verProducto, name='verproducto'),
    path('productos/formproducto/', views.formProducto, name='formproducto'),
    path('productos/modificar/<int:id>/', views.modificarProducto, name='modificarproducto'),
    path('productos/eliminar/<int:id>/', views.eliminarProducto, name='eliminarproducto'),
    path('productos/ofertas/', views.ofertaProducto, name='ofertaproducto')
]