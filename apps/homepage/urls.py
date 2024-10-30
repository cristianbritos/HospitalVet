from django.urls import path, include
from apps.homepage.views.veterinario.views import VeterinarioListView, VeterinarioCreateView, VeterinarioUpdateView
from apps.homepage.views.cliente.views import ClienteListView, ClienteCreateView, ClienteUpdateView
from apps.homepage.views.mascota.views import MascotaListView, MascotaCreateView
from apps.homepage.views.sala.views import SalaListView, SalaCreateView, SalaUpdateView
from apps.homepage.views.principal.views import PrincipalListView

urlpatterns = [
    path('veterinario/list/', VeterinarioListView.as_view(), name='veterinario-list'),
    path('veterinario/add/', VeterinarioCreateView.as_view(), name='veterinario-create'),
    path('veterinario/update/<int:pk>/', VeterinarioUpdateView.as_view(), name='veterinario-update'),  

    path('cliente/list/', ClienteListView.as_view(), name='cliente-list'),  
    path('cliente/add/', ClienteCreateView.as_view(), name='cliente-create'),
    path('cliente/update/<int:pk>/', ClienteUpdateView.as_view(), name='cliente-update'),
    
    path('mascota/list/', MascotaListView.as_view(), name='mascota-list'),  
    path('mascota/add/', MascotaCreateView.as_view(), name='mascota-create'),

    path('sala/list/', SalaListView.as_view(), name='sala-list'),  
    path('sala/add/', SalaCreateView.as_view(), name='sala-create'),
    path('sala/update/<int:pk>/', SalaUpdateView.as_view(), name='sala-update'),

    path('', PrincipalListView.as_view(), name='principal'),
]
