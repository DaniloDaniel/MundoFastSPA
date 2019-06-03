from django.contrib import admin

# Register your models here.
from .models import Producto, Usuario, Venta, DetalleVenta
admin.site.register(Usuario)

admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(DetalleVenta)