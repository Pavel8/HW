from django.shortcuts import render
from django.views.generic import TemplateView

# Jednoduchý pohled pro domovskou stránku
class HomePageView(TemplateView):
    template_name = "home.html"  # cesta k šabloně domovské stránky
