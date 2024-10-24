from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from apps.homepage.models import Veterinario

# Create your views here.

class VeterinarioListView(ListView):
    model = Veterinario
    template_name = 'veterinario/listVet.html'
   
    def get_queryset(self):
        return  Veterinario.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Lista de Veterinarios'
        return context  

class VeterinarioCreateView(CreateView):
    model = Veterinario
    template_name = 'veterinario/createVet.html'
    fields = ['nombre', 'telefono', 'direccion', 'dni']
    success_url = reverse_lazy('veterinario-list') 


class VeterinarioUpdateView(UpdateView):
    model = Veterinario
    template_name = 'veterinario/updateVet.html'
    fields = ['nombre', 'telefono', 'dni']
    success_url = reverse_lazy('veterinario-list')