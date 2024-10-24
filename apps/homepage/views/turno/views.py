
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from apps.homepage.models import Turno

# Create your views here.

class TurnoListView(ListView):
    model = Turno
    template_name = 'turno/listTurno.html'
   
    def get_queryset(self):
        return  Turno.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Turnos'
        return context  

class TurnoCreateView(CreateView):
    model = Turno
    template_name = 'turno/createTurno.html'
    fields = ['fecha', 'hora', 'mascota', 'veterinario', 'sala']
    success_url = reverse_lazy('turno-list') 