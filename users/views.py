from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import authenticate
from .forms import UserRegisterForm, UserEditForm
from users.models import Avatar
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_request(request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "Viajes/index.html")
                
        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    form.fields['username'].label = ['usuario'] 
    form.fields['password'].label = ['contraseña'] 
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})


def register(request):
    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"Viajes/index.html")
        else:
            msg_register = "Error en los datos ingresados"
            msg_register += f"{form.errors}"

    form = UserRegisterForm()
    return render(request, "users/registro.html", {"form":form, "msg_register": msg_register})

@login_required 
def editar_perfil(request):
    usuario = request.user  

    if request.method == 'POST':  
        miFormulario2 = UserEditForm(request.POST, request.FILES, instance=usuario) 

        if miFormulario2.is_valid(): 
            if miFormulario2.cleaned_data.get('imagen'):  
                if Avatar.objects.filter(user=usuario).exists():  
                    usuario.avatar.imagen = miFormulario2.cleaned_data.get('imagen')
                    usuario.avatar.save()  
                else:
                    avatar = Avatar(user=usuario, imagen=miFormulario2.cleaned_data.get('imagen'))
                    avatar.save()  

            miFormulario2.save()  

            return render(request, "Viajes/index.html")  

    else:  
        miFormulario2 = UserEditForm(instance=usuario) 

    return render(request, "users/editar_usuario.html", {"mi_form2": miFormulario2, "usuario": usuario})

class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/editar_pass.html"
    success_url = reverse_lazy("EditarPerfil")