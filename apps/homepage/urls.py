from django.urls import path, include
from apps.homepage.views import HomepageListView, HomepageCreateView, HomepageUpdateView

urlpatterns = [
    path('veterinario/list/', HomepageListView.as_view(), name='homepage-list'),
    path('veterinario/add/', HomepageCreateView.as_view(), name='homepage-create'),
    path('veterinario/update/<int:pk>/', HomepageUpdateView.as_view(), name='homepage-update')
    path('cliente/list/', HomepageClienteListView.as_view(), name='homepage-cliente-update')
]
