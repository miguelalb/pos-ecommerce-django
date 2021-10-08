from django.contrib import admin
from django.conf import settings
from django.db import models


class Promocion(models.Model):
    descripcion = models.CharField(max_length=255)
    descuento = models.FloatField()

    def __str__(self):
        return self.descripcion

    class Meta:
        ordering = ['descripcion']


class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']


class Cliente(models.Model):
    MEMBRESIA_BRONZE = 'B'
    MEMBRESIA_SILVER = 'S'
    MEMBRESIA_GOLD = 'G'

    MEMBRESIA_OPCIONES = [
        (MEMBRESIA_BRONZE, 'Bronze'),
        (MEMBRESIA_SILVER, 'Silver'),
        (MEMBRESIA_GOLD, 'Gold'),
    ]
    rnc = models.CharField(max_length=255, null=True)
    telefono = models.CharField(max_length=255, null=True)
    membresia = models.CharField(
        max_length=1, choices=MEMBRESIA_OPCIONES, default=MEMBRESIA_BRONZE)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

    class Meta:
        ordering = ['user__first_name', 'user__last_name']
