from django.db import models

# Create your models here.

class Veterinario(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre del Veterinario')    
    telefono = models.CharField(max_length=100, verbose_name='Telefono')
    direccion = models.CharField(max_length=100, verbose_name='Dirección')
    dni = models.IntegerField(default=1, null=True, blank=True, verbose_name='DNI')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Veterinario'
        verbose_name_plural = 'Veterinarios'
        ordering = ['id']


class Cliente(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre del Cliente')    
    telefono = models.CharField(max_length=100, verbose_name='Telefono')
    direccion = models.CharField(max_length=100, verbose_name='Dirección')
    dni = models.IntegerField(default=1, null=True, blank=True, verbose_name='DNI')

    def __str__(self):
        return f"Cliente: {self.nombre}, Telefono: {self.telefono}"

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


class Mascota(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre de la Mascota')    
    raza = models.CharField(max_length=100, verbose_name='Raza')    
    color = models.CharField(max_length=100, verbose_name='Color')    
    peso = models.IntegerField(default=1, null=True, verbose_name="Peso")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name='Cliente')

    def __str__(self):
        return f"Nombre: {self.nombre}, Raza: {self.raza}, Color: {self.color}"

    class Meta:
        verbose_name = 'Mascota'
        verbose_name_plural = 'Mascotas'
        ordering = ['id']


class Sala(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre de la Sala')
    ubicacion = models.CharField(max_length=100, verbose_name='Ubicación de la Sala')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'
        ordering = ['id']


class Turno(models.Model):
    fecha = models.DateField(verbose_name='Fecha del Turno')
    hora = models.TimeField(verbose_name='Hora del Turno')
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, verbose_name='Mascota')
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, verbose_name='Veterinario')
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, verbose_name='Sala')

    def __str__(self):
        return f"Turno para {self.mascota.nombre} con {self.veterinario.nombre} en la sala {self.sala.nombre}"

    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'
        ordering = ['fecha', 'hora']

class HistorialMedico(models.Model):
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, verbose_name='Mascota')
    fecha = models.DateField(verbose_name='Fecha de Consulta')
    motivo_consulta = models.CharField(max_length=255, verbose_name='Motivo de Consulta')
    diagnostico = models.TextField(verbose_name='Diagnóstico')
    tratamiento = models.TextField(verbose_name='Tratamiento')

    def __str__(self):
        return f"Historial de {self.mascota.nombre} - {self.fecha}"

    class Meta:
        verbose_name = 'Historial Médico'
        verbose_name_plural = 'Historiales Médicos'
        ordering = ['fecha']