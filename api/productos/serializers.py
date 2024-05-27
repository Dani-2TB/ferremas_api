from rest_framework import serializers

from .models import Categoria, Producto

class CategoriaSerializer(serializers.ModelSerializer):
    sub_categorias = serializers.SerializerMethodField()

    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'sub_categorias']

    def get_sub_categorias(self, obj):
        subcategorias = obj.sub_categorias.all()
        if subcategorias:
            return CategoriaSerializer(subcategorias, many=True).data
        return []

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = [
            'id', 
            'descripcion', 
            'precio', 
            'cantidad', 
            'categoria',
            ]
