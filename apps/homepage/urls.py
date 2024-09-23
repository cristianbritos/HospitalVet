from django.urls import path, include
from .views import HomepageListView

urlpatterns = [
    path('listar/', HomepageListView.as_view(), name='homepage'),
     path('listar/', HomepageListView.as_view(), name='homepage'),
]