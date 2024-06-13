from django.db import models
from django.contrib.auth.models import User


class Genero(models.Model):
    nombre = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self):
        return str(self.nombre)


class DetalleUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genero = models.ForeignKey(
        Genero,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
