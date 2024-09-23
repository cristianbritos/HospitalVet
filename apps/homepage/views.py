from django.shortcuts import render
from django.views.generic import ListView
from .models import Productos

# Create your views here.

class HomepageListView(ListView):
    model = Productos
    template_name = 'homepage/list.html'
   
    def get_queryset(self):
        return  Productos.objects.all()