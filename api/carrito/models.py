from django.db import models
from django.contrib.auth.models import User

class Carrito(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now=True)

class ItemCarrito(models.Model):
    cantidad = models.IntegerField()
    carrito = models.ForeignKey(
        Carrito,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

class Boleta(models.Model):
    total = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateTimeField(auto_now=True)