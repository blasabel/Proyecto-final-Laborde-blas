from django.urls import path
from Viajes import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobre-nosotros/', views.about, name='sobre nosotros'),     
]

#URLS para Cliente
urlpatterns += [
    path('cliente/lista', views.ClienteListView.as_view(), name="ClienteLista"),
    path('cliente/crear', views.ClienteCreateView.as_view(), name="ClienteCrear"),
    path('cliente/<int:pk>/', views.ClienteDetailView.as_view(), name="ClienteDetalle"),
    path('cliente/<int:pk>/editar', views.ClienteUpdateView.as_view(), name="ClienteEditar"),
    path('cliente/<int:pk>/eliminar', views.ClienteDeleteView.as_view(), name="ClienteEliminar")
]

#URLS para Destino
urlpatterns += [
    path('destino/lista', views.DestinoListView.as_view(), name="DestinoLista"),
    path('destino/crear', views.DestinoCreateView.as_view(), name="DestinoCrear"),
    path('destino/<int:pk>', views.DestinoDetailView.as_view(), name="DestinoDetalle"),
    path('destino/<int:pk>/editar', views.DestinoUpdateView.as_view(), name="DestinoEditar"),
    path('destino/<int:pk>/eliminar', views.DestinoDelateView.as_view(), name="DestinoEliminar")
]

#URLS para Estadia
urlpatterns += [
    path('estadia/lista', views.EstadiaListView.as_view(), name="EstadiaLista"),
    path('estadia/crear', views.EstadiaCreateView.as_view(), name="EstadiaCrear"),
    path('estadia/<int:pk>', views.EstadiaDetailView.as_view(), name="EstadiaDetalle"),
    path('estadia/<int:pk>/editar', views.EstadiaUpdateView.as_view(), name="EstadiaEditar"),
    path('estadia/<int:pk>/eliminar', views.EstadiaDeleteView.as_view(), name="EstadiaEliminar")
]