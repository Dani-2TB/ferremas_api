from django.db import models
from django.contrib.auth.models import User

class Carrito(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE
    )
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

class ItemCarrito(models.Model):
    cantidad = models.IntegerField()
    carrito = models.ForeignKey(
        Carrito,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )