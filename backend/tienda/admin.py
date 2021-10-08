from django.contrib import admin
from . import models


@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    autocomplete_fields = ['user']
    list_display = ['id', 'first_name', 'last_name', 'rnc']
