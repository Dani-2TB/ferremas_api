from django.db import models
from django.contrib.auth.models import User


class Genero(models.Model):
    nombre = models.CharField(max_length=60)

    def __str__(self):
        return str(self.nombre)


class DetalleUser(models.Model):
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    numrut = models.IntegerField(unique=True)
    
