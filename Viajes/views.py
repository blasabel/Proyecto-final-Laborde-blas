from django.shortcuts import render
from Viajes.models import Cliente, Destino, Estadia
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,CreateView,DeleteView,UpdateView,DetailView
from django.urls import reverse_lazy


# Create your views here.

def inicio(request):
    return render(request, 'Viajes/index.html')

@login_required
def about(request):
    return render(request, 'Viajes/about.html')

# def estadia(request):
#     if request.method == "POST":  
#         miFormulario3 = EstadiaFormulario(request.POST)  
#         print(miFormulario3)  

#         if miFormulario3.is_valid(): 
#             informacion3 = miFormulario3.cleaned_data  
#             estadia = Estadia(fecha_de_inicio=informacion3["fecha_de_inicio"], 
#                             fecha_de_regreso=informacion3["fecha_de_regreso"], 
#                             residencia=informacion3["residencia"],
#                             metodo_de_transporte=informacion3["metodo_de_transporte"])
                            
#             estadia.save()  
#             return render(request, "Viajes/index.html") 
#     else:
#         miFormulario3 = EstadiaFormulario()  

#     return render(request, "Viajes/estadia.html", {"miFormulario3": miFormulario3})



#CBV DE CLIENTE
#Clase para listar los clientes
class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    context_object_name = "clientes"
    template_name = "Viajes/CBV/cliente_lista.html"

#Clase para ver a detalle los clientes
class ClienteDetailView(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = "Viajes/CBV/cliente_detalle.html"

#Clase para crear clientes
class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = "Viajes/CBV/cliente_crear.html"
    success_url = reverse_lazy('ClienteLista')
    fields = ['nombre', 'apellido', 'edad', 'email']

#Clase para editar clientes
class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = "Viajes/CBV/cliente_editar.html"
    success_url = reverse_lazy('ClienteLista')
    fields = ['nombre', 'apellido', 'edad', 'email']

#Clase para eliminar clientes
class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = "Viajes/CBV/cliente_eliminar.html"
    success_url = reverse_lazy('ClienteLista')
    


#CBV DE DESTINO:
#Clase para listar los destinos
class DestinoListView(LoginRequiredMixin, ListView):
    model = Destino
    context_object_name = "destinos"
    template_name = "Viajes/CBV/destino_lista.html"

#Clase para ver a detalle los destinos
class DestinoDetailView(LoginRequiredMixin, DetailView):
    model = Destino
    template_name = "Viajes/CBV/destino_detalle.html"

#Clase para crear destinos
class DestinoCreateView(LoginRequiredMixin, CreateView):
    model = Destino
    template_name = "Viajes/CBV/destino_crear.html"
    success_url = reverse_lazy('DestinoLista')
    fields = ['ciudad', 'pais', 'aerolinea']

#Clases para editar destinos
class DestinoUpdateView(LoginRequiredMixin, UpdateView):
    model = Destino
    template_name = "Viajes/CBV/destino_editar.html"
    success_url = reverse_lazy('DestinoLista')
    fields = fields = ['ciudad', 'pais', 'aerolinea']

#Clase para eliminar destinos
class DestinoDelateView(LoginRequiredMixin, DeleteView):
    model = Destino
    template_name = "Viajes/CBV/destino_eliminar.html"
    success_url = reverse_lazy('DestinoLista')

#CBV DE ESTADIA:
#Clase para listar las estadias
class EstadiaListView(LoginRequiredMixin, ListView):
    model = Estadia
    context_object_name = "estadias"
    template_name = "Viajes/CBV/estadia_lista.html"

#Clase para ver a detalle las estadias
class EstadiaDetailView(LoginRequiredMixin, DetailView):
    model = Estadia
    template_name = "Viajes/CBV/estadia_detalle.html"

#Clase para crear estadias
class EstadiaCreateView(LoginRequiredMixin, CreateView):
    model = Estadia
    template_name = "Viajes/CBV/estadia_crear.html"
    success_url = reverse_lazy('EstadiaLista')
    fields = ['fecha_de_inicio', 'fecha_de_regreso', 'residencia', 'metodo_de_transporte']

#Clase para editar estadias
class EstadiaUpdateView(LoginRequiredMixin, UpdateView):
    model = Estadia
    template_name = "Viajes/CBV/estadia_editar.html"
    success_url = reverse_lazy('EstadiaLista')
    fields = ['fecha_de_inicio', 'fecha_de_regreso', 'residencia', 'metodo_de_transporte']

#Clase para eliminar estadias
class EstadiaDeleteView(LoginRequiredMixin, DeleteView):
    model = Estadia
    template_name = "Viajes/CBV/estadia_eliminar.html"
    success_url = reverse_lazy('EstadiaLista')


