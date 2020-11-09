from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)

    def _str_(self):
        return self.nombre



class Cafe(models.Model):
    nombre_cafe = models.CharField(max_length=100)
    valor = models.IntegerField()
    tamaño = models.CharField(max_length=100)

    def _str_(self):
        return self.nombre
