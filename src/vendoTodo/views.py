from django.shortcuts import render
from django.views.generic import ListView
from productos.models import Producto

def home(request):
   
      return render(request, "index.html",{})
    




