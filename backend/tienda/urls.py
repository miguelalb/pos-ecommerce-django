from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.producto_list),
    path('productos/<pk>/', views.producto_detail),
    path('categorias/', views.categoria_list),
    path('categorias/<pk>/', views.categoria_detail),
]
