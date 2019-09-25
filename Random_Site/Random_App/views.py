# Random_Site/Random_App/views.py
from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView

# Add the two views we have been talking about  all this time :)
class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
"""
from django.shortcuts import render

# Create your views here.

def home(request):
        return render(request, 'Random_App/home.html')
        """
