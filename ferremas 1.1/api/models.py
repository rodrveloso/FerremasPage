from django.db import models

class Producto(models.Model):
    id = models.CharField(max_length=12, primary_key=True) 
    nombre = models.CharField(max_length=50)
    imagen = models.CharField(max_length=200)
    existencia = models.IntegerField()
    descripcion = models.CharField( max_length=300)
    precio = models.FloatField()
# Create your models here.
