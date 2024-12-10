from django.db import models

# Create your models here.


# aqui se crean los modelos (las tablas o colecciones)
class programmer(models.Model): 
    fullname = models.CharField(max_length=50),
    nicknime = models.CharField(max_length=30),
    age = models.PositiveSmallIntegerField(default=True),
    phone = models.CharField(max_length=10,null=True, default=None),
    is_active = models.BooleanField(default=True),


class Aprendiz(models.Model):
    nombre = models.CharField(max_length=20),
    apellido = models.CharField(max_length=20),
    sexo = models.CharField(max_length=1),
    num_ficha = models.CharField(max_length=7),
    formacion = models.BooleanField(default=True),
    fecha_ingreso = models.DateTimeField(auto_now=True),
    activo = models.BooleanField(default=True)