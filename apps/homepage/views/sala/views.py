from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from apps.homepage.models import Sala

# Create your views here.

class SalaListView(ListView):
    model = Sala
    template_name = 'sala/list.html'
   
    def get_queryset(self):
        return  Sala.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Lista de Salas'
        return context  

class SalaCreateView(CreateView):
    model = Sala
    template_name = 'sala/create2.html'
    fields = ['nombre', 'ubicacion']
    success_url = reverse_lazy('sala-list') 


class SalaUpdateView(UpdateView):
    model = Sala
    template_name = 'sala/create2.html'
    fields = ['nombre', 'ubicacion']
    success_url = reverse_lazy('sala-list')
