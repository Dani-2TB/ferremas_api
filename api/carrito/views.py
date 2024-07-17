from rest_framework.views import APIView
from rest_framework.response import Response
from .service import Cart
from rest_framework import status
from .models import Carrito, ItemCarrito
from .serializers import (
    CarritoSerializer, ItemCarritoSerializer
    )
from django.http import Http404 


class CrearCarrito(APIView):
    # Obtener objeto desde la BD
    def post(self, request, format=None):
        carrito_serializer = CarritoSerializer(data=request.data.carrito)
        for producto in request.data.items:
            new_producto = ItemCarritoSerializer(producto)
            new_producto.save()
        if carrito_serializer.is_valid():
            carrito_serializer.save()
            return Response(carrito_serializer.data, status=status.HTTP_200_OK)
        return Response(carrito_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarritoDetalle(APIView):
    def get_object(self, pk):
        try:
            return Carrito.objects.get(pk=pk)
        except Carrito.DoesNotExist:
            raise Http404
    # Obtener carrito
    def get(self, request, pk, format=None):
        producto = Carrito.objects.get(pk=pk)
        serializer = CarritoSerializer(producto)
        return Response(serializer.data)

    # Update carrito
    def put(self, request, pk, format=None):
        producto = self.get_object(pk)

        serializer = CarritoSerializer(producto, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

