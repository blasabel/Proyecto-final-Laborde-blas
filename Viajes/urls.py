from django.urls import path
from Viajes import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('cliente/', views.cliente, name='cliente'),
    path('destino/', views.destino, name='destino'),
    path('estadia/', views.estadia, name='estadia'),
    

]