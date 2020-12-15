from django.urls import path
from .views import HomeView, AboutView, SnackDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('details/<int:pk>/', SnackDetailView.as_view(), name="snack_detail"),
]
