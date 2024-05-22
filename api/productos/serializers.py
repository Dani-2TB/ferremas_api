from rest_framework.serializers import ModelSerializer

from .models import Categoria, Subcategoria, Producto

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id','nombre']

class SubcategoriaSerializer(ModelSerializer):
    class Meta:
        model = Subcategoria
        fields = ['id','nombre', 'categoria']

class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = [
            'id', 
            'descripcion', 
            'precio', 
            'cantidad', 
            'categoria', 
            'subcategoria'
            ]
