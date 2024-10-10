from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cupon(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    descripcion = models.TextField()
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_expiracion = models.DateField(blank=True)
    es_activo = models.BooleanField(default=True)

    def __str__(self):
        return self.codigo
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre + self.apellido

class Cliente(models.Model):
    nombreEmpresa = models.CharField(max_length=30)

    def __str__(self):
        return self.nombreEmpresa

class CuponCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cupon = models.ForeignKey(Cupon, on_delete=models.CASCADE)

class CuponUsuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cupon = models.ForeignKey(Cupon, on_delete=models.CASCADE)
    fecha_obtenido = models.DateTimeField(auto_now_add=True)
    usado = models.BooleanField(default=False)