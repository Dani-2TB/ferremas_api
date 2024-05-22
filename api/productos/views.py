from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

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