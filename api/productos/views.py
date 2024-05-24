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

# CRUD Categoría
class CategoriaList(APIView):
    def post(self, request, format=None):
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

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

# CRUD Subcategoría
from .serializers import SubcategoriaSerializer
from .models import Subcategoria

class SubcategoriaList(APIView):
    def post(self, request, format=None):
        serializer = SubcategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        subcategorias = Subcategoria.objects.all()
        serializer = SubcategoriaSerializer(subcategorias, many=True)
        return Response(serializer.data)

class SubcategoriaDetalle(APIView):

    def get_object(self, pk):
        try:
            return Subcategoria.objects.get(pk=pk)
        except Subcategoria.DoesNotExist:
            raise Http404
    
    # Leer subcategoria
    def get(self, request, pk, format=None):
        subcategoria = self.get_object(pk)
        serializer = SubcategoriaSerializer(subcategoria)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Update subcategoria
    def put(self, request, pk, format=None):
        subcategoria = self.get_object(pk)
        data = request.data
        # Agregamos la id de la categoria desde el backend, para modificar
        # subcategoria sólo con el ID
        data["categoria"] = subcategoria.categoria.pk
        serializer = SubcategoriaSerializer(subcategoria, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Borrar subcategoria
    def delete(self, request, pk, format=None):
        subcategoria = self.get_object(pk)
        subcategoria.delete()
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
        return Response(serializer.data,status=status.HTTP_200_OK)

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