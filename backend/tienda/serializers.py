from rest_framework import serializers
from .models import Categoria, Producto


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'sku', 'slug', 'nombre', 'descripcion', 'inventario',
                  'costo', 'margen', 'precio', 'rating', 'stock', 'categoria']

    stock = serializers.SerializerMethodField(method_name='calc_stock')

    def calc_stock(self, producto: Producto):
        if producto.inventario <= 5:
            return 'BAJO'
        return 'OK'
