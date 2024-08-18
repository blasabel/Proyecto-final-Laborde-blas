from django.shortcuts import render
from Viajes.forms import ClienteFormulario, DestinoFormulario, EstadiaFormulario
from Viajes.models import Cliente, Destino, Estadia

# Create your views here.

def inicio(request):
    return render(request, 'Viajes/index.html')

def cliente(request):
    if request.method == "POST":  
        miFormulario = ClienteFormulario(request.POST)  
        print(miFormulario)  

        if miFormulario.is_valid(): 
            informacion = miFormulario.cleaned_data  
            curso = Cliente(nombre=informacion["nombre"], 
                            apellido=informacion["apellido"], 
                            edad=informacion["edad"], 
                            email=informacion["email"])  
            curso.save()  
            return render(request, "Viajes/index.html") 
    else:
        miFormulario = ClienteFormulario()  

    return render(request, "Viajes/cliente.html", {"miFormulario": miFormulario})
    
def destino(request):
    return render(request, 'Viajes/destino.html')

def estadia(request):
    return render(request, 'Viajes/estadia.html')
