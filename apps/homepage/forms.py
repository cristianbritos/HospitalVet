from django import forms
from apps.homepage.models import Mascota, Cliente, Veterinario, Turno, Sala

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'raza', 'peso', 'cliente']

    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all())


class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ['fecha', 'hora', 'mascota','sala', 'veterinario' ]


    
    mascota = forms.ModelChoiceField(queryset=Mascota.objects.all())
    sala = forms.ModelChoiceField(queryset=Sala.objects.all())
    veterinario = forms.ModelChoiceField(queryset=Veterinario.objects.all())
