from django.shortcuts import render
from Viajes.forms import ClienteFormulario, DestinoFormulario, EstadiaFormulario
from Viajes.models import Cliente, Destino, Estadia
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    return render(request, 'Viajes/index.html')

def about(request):
    return render(request, 'Viajes/about.html')

@login_required
def cliente(request):
    if request.method == "POST":  
        miFormulario = ClienteFormulario(request.POST)  
        print(miFormulario)  

        if miFormulario.is_valid(): 
            informacion = miFormulario.cleaned_data  
            cliente = Cliente(nombre=informacion["nombre"], 
                            apellido=informacion["apellido"], 
                            edad=informacion["edad"], 
                            email=informacion["email"])  
            cliente.save()  
            return render(request, "Viajes/index.html") 
    else:
        miFormulario = ClienteFormulario()  

    return render(request, "VIajes/cliente.html", {"miFormulario": miFormulario})

@login_required
def destino(request):
    if request.method == "POST":  
        miFormulario2 = DestinoFormulario(request.POST)  
        print(miFormulario2)  

        if miFormulario2.is_valid(): 
            informacion2 = miFormulario2.cleaned_data  
            destino = Destino(ciudad=informacion2["ciudad"], 
                            pais=informacion2["pais"], 
                            aerolinea=informacion2["aerolinea"])
                            
            destino.save()  
            return render(request, "Viajes/index.html") 
    else:
        miFormulario2 = DestinoFormulario()  

    return render(request, "Viajes/destino.html", {"miFormulario2": miFormulario2})

@login_required
def estadia(request):
    if request.method == "POST":  
        miFormulario3 = EstadiaFormulario(request.POST)  
        print(miFormulario3)  

        if miFormulario3.is_valid(): 
            informacion3 = miFormulario3.cleaned_data  
            estadia = Estadia(fecha_de_inicio=informacion3["fecha_de_inicio"], 
                            fecha_de_regreso=informacion3["fecha_de_regreso"], 
                            residencia=informacion3["residencia"],
                            metodo_de_transporte=informacion3["metodo_de_transporte"])
                            
            estadia.save()  
            return render(request, "Viajes/index.html") 
    else:
        miFormulario3 = EstadiaFormulario()  

    return render(request, "Viajes/estadia.html", {"miFormulario3": miFormulario3})

@login_required
def buscarciudad(request):
    return render(request, "Viajes/buscarFormulario.html")

def buscar(request):
    
    if request.GET["ciudad"]:
        ciudad = request.GET['ciudad']
        pais = Destino.objects.filter(ciudad__icontains=ciudad)

        return render(request, "Viajes/buscarFormulario.html", {"pais":pais, "ciudad":ciudad} )
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)