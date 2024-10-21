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
    direccion = models.CharField(max_length=255, verbose_name='Direccion')
    dni = models.CharField(max_length=20, null=True, blank=True, verbose_name='DNI')

class Mascota(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre de la Mascota')
    especie = models.CharField(max_length=100, verbose_name='Especie')
    raza = models.CharField(max_length=100, verbose_name='Raza', null=True, blank=True)
    edad = models.PositiveIntegerField(verbose_name='Edad', null=True, blank=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Peso (kg)', null=True, blank=True)
    fecha_ingreso = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Ingreso')
    clientefk = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    veterinariofk =  models.ForeignKey(Veterinario, on_delete=models.CASCADE, verbose_name='Veterinario')

class Turno(models.Model):
    mascotafk = models.ForeignKey(Mascota, on_delete=models.CASCADE, verbose_name='Mascota')
    veterinariofk =  models.ForeignKey(Veterinario, on_delete=models.CASCADE, verbose_name='Veterinario') 
    clientefk =  models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')
    fecha = models.DateField(verbose_name='Fecha del Turno')
    hora = models.TimeField(verbose_name='Hora del  Turno')
    motivo = models.CharField(max_length=255, verbose_name='Motivo del Turno')