from django.contrib import admin
from .models import Veterinario
from .models import Cliente

# Register your models here.
admin.site.register(Veterinario)
admin.site.register(Cliente)