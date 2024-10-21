from django.urls import path, include
from apps.homepage.views import HomepageListView, HomepageCreateView, HomepageUpdateView


urlpatterns = [
    path('list/', HomepageListView.as_view(), name='homepage-list'),
    path('add/', HomepageCreateView.as_view(), name='homepage-create'),
    path('update/<int:pk>/', HomepageUpdateView.as_view(), name='homepage-update')
]

