from django.urls import path

from . import views

app_name = 'MundoFastWebApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('productos/crearproducto/', views.crearProducto, name='crearproducto'),
    path('productos/<int:id>/', views.verProducto, name='verproducto'),
    path('productos/formproducto/', views.formProducto, name='formproducto')
]