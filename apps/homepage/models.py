from django.db import models

# Create your models here.

class Veterinario(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre del Veterinario')    
    telefono = models.CharField(max_length=100, verbose_name='Telefono')
    direccion = models.CharField(max_length=100, verbose_name='Direccion')
    dni = models.IntegerField(default=1, null=True, blank=True)




    