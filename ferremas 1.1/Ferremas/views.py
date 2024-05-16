from django.shortcuts import render
from api.models import Producto

def home(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})
