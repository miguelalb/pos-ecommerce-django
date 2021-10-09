from django.contrib import admin
from . import models


@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['id', 'first_name', 'last_name', 'rnc']


@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    autocomplete_fields = ['producto_destacado']


@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    search_fields = ['nombre']


admin.site.register(models.Promocion)
