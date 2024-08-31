from django.urls import path
from Viajes import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobre-nosotros/', views.about, name='sobre nosotros'),
    path('cliente/', views.cliente, name='cliente'),
    path('destino/', views.destino, name='destino'),
    path('estadia/', views.estadia, name='estadia'),
    path('buscarciudad/', views.buscarciudad, name='Buscar'),
    path('buscar/', views.buscar),
]