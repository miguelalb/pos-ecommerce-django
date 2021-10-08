from django.conf import settings
from django.db import models


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

    class Meta:
        ordering = ['user__first_name', 'user__last_name']
