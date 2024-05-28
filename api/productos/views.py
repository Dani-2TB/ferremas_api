from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404

# Raiz del endpoint para propósitos de testeo
class ProductosRoot(APIView):
    def get(self, request):
        return Response({"message":"Raiz el endpoint productos!"})


from .serializers import CategoriaSerializer
from .models import Categoria

# Vistas de Categoria
class CategoriaList(APIView):
    def post(self, request, format=None):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, solicitud, formato=None):
        categorias_principales = Categoria.objects.filter(categoria_madre=None)
        serializer = CategoriaSerializer(categorias_principales, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CategoriaDetalle(APIView):

    def get_object(self, pk):
        try:
            return Categoria.objects.get(pk=pk)
        except Categoria.DoesNotExist:
            raise Http404
    
    # Leer categoria
    def get(self, request, pk, format=None):
        categoria = self.get_object(pk)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Update categoria
    def put(self, request, pk, format=None):
        categoria = self.get_object(pk)
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Borrar categoria
    def delete(self, request, pk, format=None):
        categoria = self.get_object(pk)
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Vistas de Producto
from .models import Producto
from .serializers import ProductoSerializer

class ProductoList(APIView):
    def post(self, request, format=None):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

class ProductoDetalle(APIView):
    # Obtener objeto desde la BD
    def get_object(self, pk):
        try:
            return Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            raise Http404
    
    # Obtener producto
    def get(self, request, pk, format=None):
        producto = Producto.objects.get(pk=pk)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)

    # Update producto
    def put(self, request, pk, format=None):
        producto = self.get_object(pk)

        serializer = ProductoSerializer(producto, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Borrar producto
    def delete(self, request, pk, format=None):
        producto = self.get_object(pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductoCategoriaList(APIView):
    def get_objects(self, id_categoria):
        try:
            return Producto.objects.filter(categoria = id_categoria) 
        except Producto.DoesNotExist:
            raise Http404

    def get(self, request, id_categoria):
        productos = self.get_objects(id_categoria)
        serializer = ProductoSerializer(productos, many=True)
        if serializer.data == []:
            return Response({'error': 'Not found'}, status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)