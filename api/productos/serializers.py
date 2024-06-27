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
    nombre_categoria = serializers.CharField(source='categoria.nombre')
    nombre_marca = serializers.CharField(source='marca.nombre', allow_null=True)

    class Meta:
        model = Producto
        fields = [
            'id',
            'nombre',
            'descripcion',
            'precio',
            'cantidad',
            'nombre_categoria',
            'nombre_marca'
        ]
