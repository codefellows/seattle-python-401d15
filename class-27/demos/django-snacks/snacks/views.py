from django.views.generic import TemplateView, ListView, DetailView
from .models import Snack

class HomeView(ListView):
    template_name = 'home.html'
    model = Snack

class AboutView(TemplateView):
    template_name="about.html"

class SnackDetailView(DetailView):
    template_name = 'snack-detail.html'
    model = Snack
