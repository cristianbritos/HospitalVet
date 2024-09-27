from django.urls import path, include
from apps.homepage.views  import HomepageListView

urlpatterns = [
    path('veterinario/', HomepageListView.as_view(), name='homepage'),
]
