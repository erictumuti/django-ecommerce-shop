from django.shortcuts import render
from django.views.generic import ListView, DetailView

from App_Shop.models import Product
# Create your views here.

class Home(ListView):
    model = Product
    template_name = 'App_Shop/Home.html'
