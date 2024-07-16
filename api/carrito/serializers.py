from rest_framework import serializers

from .models import Carrito, ItemCarrito

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = [
            'id',
            'total',
            'cantidad',
        ]