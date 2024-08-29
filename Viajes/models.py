from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.edad} {self.email}"

class Destino(models.Model):
    ciudad = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    aerolinea = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.ciudad} {self.pais} {self.aerolinea}"

class Estadia(models.Model):
    fecha_de_inicio = models.DateField()
    fecha_de_regreso = models.DateField()
    residencia = models.CharField(max_length=40)
    metodo_de_transporte = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.fecha_de_inicio} {self.fecha_de_regreso} {self.residencia} {self.metodo_de_transporte}"


