from django.shortcuts import render
from django.views.generic import ListView
from .models import Veterinario

# Create your views here.

class HomepageListView(ListView):
    model = Veterinario
    template_name = 'homepage/list.html'
   
    def get_queryset(self):
        return  Veterinario.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context  