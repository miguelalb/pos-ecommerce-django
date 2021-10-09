from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Producto
from .serializers import ProductoSerializer


@api_view()
def producto_list(request):
    queryset = Producto.objects.all()
    serializer = ProductoSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    serializer = ProductoSerializer(producto)
    return Response(serializer.data)
