from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'Viajes/index.html')

def cliente(request):
    return render(request, 'Viajes/cliente.html')

def destino(request):
    return render(request, 'Viajes/destino.html')

def estadia(request):
    return render(request, 'Viajes/estadia.html')