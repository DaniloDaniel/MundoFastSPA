from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings
from .managers import CustomUserManager


from django.core.validators import MaxValueValidator
import datetime

# Create your models here.
class Producto(models.Model):
    catElectrodomesticos = 'Electrodomésticos'
    catCocina = 'Cocina'
    catBanio = 'Baño'
    catDecoracion = 'Decoración'
    catJardineria = 'Jardín'
    catOtros = 'Otros'
    opcionesCategoria = (
        (catElectrodomesticos, 'Electrodomésticos'),
        (catCocina, 'Artículos de Cocina'),
        (catBanio, 'Artículos de Baño'),
        (catDecoracion, 'Artículos de Decoracion'),
        (catJardineria, 'Artículos de Jardineria'),
        (catOtros, 'Otros')
    )

    codigoProducto = models.IntegerField(unique=True)
    nombreProducto = models.CharField(max_length=100)
    descripcionProducto = models.CharField(max_length=500)
    imagenProducto = models.ImageField(upload_to='productos', default='Imagen-no-disponible.png')
    categoriaProducto = models.CharField(max_length=50, choices=opcionesCategoria, default=catElectrodomesticos)
    precioProducto = models.PositiveIntegerField(default=0)
    cantidadProducto = models.PositiveIntegerField(default=0)
    ofertaProducto = models.BooleanField(default=False)
    descuentoProducto = models.PositiveIntegerField(default = 0, validators = [MaxValueValidator(100)])

    def __str__(self):
        return self.nombreProducto
    
class Usuario(AbstractBaseUser, PermissionsMixin):
    rolAdministrador = 'Administrador'
    rolDesarrollador = 'Desarrollador'
    rolEmpleado = 'Empleado'
    rolCajero = 'Cajero'
    rolCliente = 'Cliente'
    rolOtro = 'Otro'
    opcionesRol = (
        (rolAdministrador, 'Administrador'),
        (rolDesarrollador, 'Desarrollador'),
        (rolEmpleado, 'Empleado'),
        (rolCajero, 'Cajero'),
        (rolCliente, 'Cliente'),
        (rolOtro, 'Otro')
    )
    rutUsuario = models.CharField(max_length=20)
    nombreUsuario = models.CharField(max_length=50)
    imagenUsuario = models.ImageField(upload_to='usuarios', default='Imagen-no-disponible.png')
    rolUsuario = models.CharField(max_length=50, choices=opcionesRol, default=rolDesarrollador)
    emailUsuario = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser= models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'emailUsuario'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.emailUsuario

class Venta(models.Model):
    folioVenta = models.PositiveIntegerField(unique=True, default=0)
    fechaVenta = models.DateTimeField(auto_now_add=True)
    cuotasVenta = models.PositiveIntegerField(default=1)
    subTotal = models.PositiveIntegerField(default=0)
    totalVenta = models.PositiveIntegerField()
    estadoVenta = models.CharField(max_length=20, default='En Proceso')
    responsableVenta = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    descuendoAdicionalVenta = models.PositiveIntegerField(default = 0, validators = [MaxValueValidator(100)])
    productos = models.ManyToManyField(Producto, through='DetalleVenta')

    def __str__(self):
        return ("Venta Folio N°" + str(self.folioVenta) )

class DetalleVenta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    cantidadProducto = models.PositiveIntegerField(default=1)
    descuentoAplicadoProducto = models.PositiveIntegerField(default = 0, validators = [MaxValueValidator(100)])
    totalPorProducto = models.PositiveIntegerField()

    def __str__(self):
        return (str(self.venta) + " " +str(self.producto))

    def totalProducto(self):
        total = self.cantidadProducto * self.totalPorProducto
        return total

class Empresa(models.Model):
    nombreEmpresa = models.CharField(max_length=30, default="")
    emailEmpresa = models.CharField(max_length=1000, default="")
    descripcionEmpresa = models.CharField(max_length=10000 ,default="")
    imagenEmpresa = models.CharField(max_length=10000, default="")
    direccionEmpresa = models.CharField(max_length=50, default="")
    horarioEmpresa = models.CharField(max_length=500, default="")

    def __str__(self):
        return self

image = models.ImageField(upload_to='img')