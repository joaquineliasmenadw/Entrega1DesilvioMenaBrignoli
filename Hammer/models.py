from django.db import models
from datetime import *
# Create your models here.
class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    provincia = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=250)
    empleado = models.CharField(max_length= 245)
    precio = models.FloatField()
    active = models.BooleanField(default=True)
    

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    experiencia= models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=250)
    telefono = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
class Empleador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    provincia = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=250)
    telefono = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)