from django import forms

class ClienteFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    email = forms.EmailField()

class DestinoFormulario(forms.Form):
    ciudad = forms.CharField(max_length=40)
    pais = forms.CharField(max_length=40)
    aerolinea = forms.CharField(max_length=40)

class EstadiaFormulario(forms.Form):
    fecha_de_inicio = forms.DateField()
    fecha_de_regreso = forms.DateField()
    residencia = forms.CharField(max_length=40)
    metodo_de_transporte = forms.CharField(max_length=40)

