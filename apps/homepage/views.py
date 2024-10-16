from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import Veterinario

# Create your views here.

class HomepageListView(ListView):
    model = Veterinario
    template_name = 'homepage/list.html'
   
    def get_queryset(self):
        return  Veterinario.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Lista de Veterinarios'
        return context  

class HomepageCreateView(CreateView):
    model = Veterinario
    template_name = 'homepage/create2.html'
    fields = ['nombre', 'telefono', 'direccion', 'dni']
    success_url = reverse_lazy('homepage-list') 


class HomepageUpdateView(UpdateView):
    model = Veterinario
    template_name = 'homepage/create.html'
    fields = ['nombre', 'telefono', 'dni']
    success_url = reverse_lazy('homepage-list')

