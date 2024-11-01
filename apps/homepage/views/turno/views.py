from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from apps.homepage.models import Turno
from apps.homepage.forms import TurnoForm
# Create your views here.

class TurnoListView(ListView):
    model = Turno
    template_name = 'turno/list.html'
   
    def get_queryset(self):
        return  Turno.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Lista de Turnos'
        return context  

class TurnoCreateView(CreateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'turno/create2.html'
    #fields = [ 'fecha', 'hora' ]
    success_url = reverse_lazy('turno-list') 
