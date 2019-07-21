from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings
from .managers import CustomUserManager
from django_resized import ResizedImageField
from django.core.files.storage import FileSystemStorage
import os
from django.core.validators import MaxValueValidator
import datetime

def content_file_name(instance, filename):
    # Funcion que se encarga de asignar nombre al archivo a crear
    # El archivo sera subido a MEDIA_ROOT/<user_<id>.PNG
    if(isinstance(instance,Usuario)):
        return 'usuarios/{0}'.format(str(instance.id) + '.PNG')
    elif(isinstance(instance,Producto)):
        return 'productos/{0}'.format(str(instance.id) + '.PNG')
    # Caso default para futuro
    return '/{0}'.format(str(instance.id) + '.PNG')

class OverwriteStorage(FileSystemStorage):
    # Funcion que habilita la sobreescritura de archivos
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

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
    imagenProducto = ResizedImageField(upload_to=content_file_name, default='Imagen-no-disponible.png', size=[500, 300], storage=OverwriteStorage())
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
    imagenUsuario = ResizedImageField(upload_to=content_file_name, default='Imagen-no-disponible.png', size=[500, 300], storage=OverwriteStorage())
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