from django.contrib import admin
from .models import Veterinario
from .models import Cliente
from .models import Mascota
from .models import Turno


# Register your models here.
admin.site.register(Veterinario)
admin.site.register(Cliente)
admin.site.register(Mascota)
admin.site.register(Turno)

