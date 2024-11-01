from django import forms
from apps.homepage.models import Mascota, Cliente, Veterinario

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'raza', 'peso', 'cliente']

    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all())


