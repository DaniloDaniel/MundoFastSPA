from django.db import models

# Create your models here.
class Usuario(models.Model):
    rutUsuario = models.CharField(max_length=20)
    nombreUsuario = models.CharField(max_length=50)
    emailUsuario = models.CharField(max_length=100)
    imagenUsuario = models.CharField(max_length=10000)
    rolUsuario = models.CharField(max_length=20)
    passwordUsuario = models.CharField(max_length=50)

    def __str__(self):
        return self.rutUsuario