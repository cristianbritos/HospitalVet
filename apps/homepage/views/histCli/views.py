from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from apps.homepage.models import HistMedEnc, Veterinario
from apps.homepage.forms import HistMedForm

# Create your views here.

class HistMedEncListView(ListView):
    model = HistMedEnc
    template_name = 'histCli/list.html'
   
    def get_queryset(self):
        return  HistMedEnc.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Lista de Historias Clinicas'
        return context

class HistMedEncCreateView(CreateView):
    model = HistMedEnc
    form_class = HistMedForm
    template_name = 'histCli/create2.html'
    success_url = reverse_lazy('histCli-list') 

class HistMedEncUpdateView(UpdateView):
    model = HistMedEnc
    form_class = HistMedForm
    template_name = 'histCli/create2.html'
    success_url = reverse_lazy('histCli-list')
