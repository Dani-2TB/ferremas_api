from rest_framework import serializers

from .models import Carrito, ItemCarrito

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = "__all__"

class ItemCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"


class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"