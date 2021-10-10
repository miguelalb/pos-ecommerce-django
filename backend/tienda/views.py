from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer


@api_view()
def producto_list(request):
    queryset = Producto.objects.select_related('categoria').all()
    serializer = ProductoSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    serializer = ProductoSerializer(producto)
    return Response(serializer.data)


@api_view()
def categoria_list(request):
    queryset = Categoria.objects.all()
    serializer = CategoriaSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def categoria_detail(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    serializer = CategoriaSerializer(categoria)
    return Response(serializer.data)
