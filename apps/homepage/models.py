from django.db import models

# Create your models here.

class Veterinario(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre del Veterinario')    
    telefono = models.CharField(max_length=100, verbose_name='Telefono')
    direccion = models.CharField(max_length=100, verbose_name='Dirección')
    dni = models.IntegerField(default=1, null=True, blank=True, verbose_name='DNI')

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre del Cliente')
    apellido = models.CharField(max_length=100, verbose_name='Apellido del Cliente')
    telefono = models.CharField(max_length=15, verbose_name='Teléfono')
    email = models.EmailField(unique=True, verbose_name='Correo Electrónico')
    direccion_calle = models.CharField(max_length=255, verbose_name='Calle')
    direccion_numero = models.CharField(max_length=10, verbose_name='Número')
    direccion_ciudad = models.CharField(max_length=100, verbose_name='Ciudad')
    direccion_estado = models.CharField(max_length=100, verbose_name='Estado/Provincia')
    direccion_codigo_postal = models.CharField(max_length=20, verbose_name='Código Postal')
    dni = models.CharField(max_length=20, null=True, blank=True, verbose_name='DNI')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"    