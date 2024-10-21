from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from .models import Veterinario
from .models import Cliente
from .models import Mascota
from .models import Turno



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

#Cliente
class HomepageListView(ListView):
    model = Cliente
    template_name = 'homepage/list.html'
   
    def get_queryset(self):
        return  Cliente.objects.all()
    
#Mascota (Animal)
class HomepageListView(ListView):
    model = Mascota
    template_name = 'homepage/list.html'
   
    def get_queryset(self):
        return  Mascota.objects.all()
    
#Turno
class HomepageListView(ListView):
    model = Turno
    template_name = 'homepage/list.html'
   
    def get_queryset(self):
        return  Turno.objects.all()