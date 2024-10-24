from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from apps.homepage.models import Veterinario

# Create your views here.

class PrincipalListView(ListView):
    model = Veterinario
    template_name = 'principal/index.html'
   
    def get_queryset(self):
        return  Veterinario.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Pagina Principal'
        return context  
