from django.db import models

from django.core.validators import MaxValueValidator
import datetime

# Create your models here.
class Producto(models.Model):
    catElectrodomesticos = 'Electro'
    catCocina = 'Cocina'
    catBanio = 'Baño'
    catDecoracion = 'Decoración'
    catJardineria = 'Jardín'
    opcionesCategoria = (
        (catElectrodomesticos, 'Electrodomesticos'),
        (catCocina, 'Articulos de Cocina'),
        (catBanio, 'Articulos de Baño'),
        (catDecoracion, 'Articulos de Decoracion'),
        (catJardineria, 'Articulos de Jardineria')
    )

    codigoProducto = models.IntegerField(unique=True)
    nombreProducto = models.CharField(max_length=100)
    descripcionProducto = models.CharField(max_length=500)
    categoriaProducto = models.CharField(max_length=50, choices=opcionesCategoria, default=catElectrodomesticos)
    precioProducto = models.PositiveIntegerField(default=0)
    cantidadProducto = models.PositiveIntegerField(default=0)
    ofertaProducto = models.BooleanField(default=False)
    descuentoProducto = models.PositiveIntegerField(default = 0, validators = [MaxValueValidator(100)])

    def __str__(self):
        return self.nombreProducto
    
class Usuario(models.Model):
    rutUsuario = models.CharField(max_length=20)
    nombreUsuario = models.CharField(max_length=50)
    emailUsuario = models.CharField(max_length=100)
    imagenUsuario = models.CharField(max_length=10000)
    rolUsuario = models.CharField(max_length=20)
    passwordUsuario = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreUsuario

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