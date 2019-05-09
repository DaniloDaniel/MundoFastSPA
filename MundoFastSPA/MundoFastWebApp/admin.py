from django.contrib import admin

# Register your models here.
from .models import Producto, Usuario
admin.site.register(Usuario)

admin.site.register(Producto)