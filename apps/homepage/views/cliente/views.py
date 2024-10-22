from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from apps.homepage.models import Cliente

# Create your views here.

class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/list.html'
   
    def get_queryset(self):
        return  Cliente.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Lista de Clientes'
        return context  

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'cliente/create2.html'
    fields = ['nombre', 'telefono', 'direccion', 'dni']
    success_url = reverse_lazy('cliente-list') 


class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = 'cliente/create2.html'
    fields = ['nombre', 'telefono', 'dni']
    success_url = reverse_lazy('cliente-list')