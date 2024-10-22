from django.urls import path, include
from apps.homepage.views.veterinario.views import VeterinarioListView, VeterinarioCreateView, VeterinarioUpdateView
from apps.homepage.views.cliente.views import ClienteListView, ClienteCreateView, ClienteUpdateView

urlpatterns = [
    path('veterinario/list/', VeterinarioListView.as_view(), name='veterinario-list'),
    path('veterinario/add/', VeterinarioCreateView.as_view(), name='veterinario-create'),
    path('veterinario/update/<int:pk>/', VeterinarioUpdateView.as_view(), name='veterinario-update'),  

    path('cliente/list/', ClienteListView.as_view(), name='cliente-list'),  
    path('cliente/add/', ClienteCreateView.as_view(), name='cliente-create'),
    path('cliente/update/<int:pk>/', ClienteUpdateView.as_view(), name='cliente-update'),
]
