from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    telefono = models.CharField(max_length=10)
    fecha_nacimiento = models.DateTimeField()

class Alumno(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    jornada = models.CharField(max_length=40)
    Codifo = models.IntegerField(max_length=10)