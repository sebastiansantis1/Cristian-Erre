from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):

    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', 'Administrador'
        CLIENTE = 'CLIENTE', 'Cliente'

    # Sobrescribimos el email para que sea único
    email = models.EmailField('correo electrónico', unique=True)

    # Rol del usuario dentro del sistema
    rol = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.CLIENTE,
        verbose_name='rol'
    )

    def __str__(self):
        # Mostramos algo útil cuando se imprima el usuario
        return f"{self.username} ({self.email})"
