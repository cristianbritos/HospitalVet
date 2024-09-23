from django.db import models

# Create your models here.

class Productos(models.Model):
    articulo = models.CharField(max_length=100, verbose_name='Nombre del producto')
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()

    