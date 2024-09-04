from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('registrar/', views.register, name="Registrar"),
    path('logout/', views.cerrar_sesion, name="Logout"),
    path('editar/', views.editar_perfil, name="EditarPerfil"),
    path('cambiar_contraseña/', views.CambiarContrasenia.as_view(), name="CambiarContraseña"),
]