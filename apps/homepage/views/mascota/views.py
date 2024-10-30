
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from apps.homepage.models import Mascota

# Create your views here.

class MascotaListView(ListView):
    model = Mascota
    template_name = 'mascota/list.html'
   
    def get_queryset(self):
        return  Mascota.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Lista de Mascotas'
        return context  

class MascotaCreateView(CreateView):
    model = Mascota
    template_name = 'mascota/create2.html'
    fields = ['nombre', 'raza', 'color', 'peso']
    success_url = reverse_lazy('mascota-list') 
