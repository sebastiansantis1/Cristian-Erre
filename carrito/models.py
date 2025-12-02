from django.db import models
from django.conf import settings
from obras.models import Obra


class Carrito(models.Model):

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='carritos'
    )

    session_key = models.CharField(max_length=40, null=True, blank=True)

    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.usuario:
            return f"Carrito de {self.usuario.username}"
        return f"Carrito de sesión {self.session_key}"

    def total(self):

        return sum(item.subtotal() for item in self.items.all())


class ItemCarrito(models.Model):

    carrito = models.ForeignKey(
        Carrito,
        on_delete=models.CASCADE,
        related_name='items'
    )

    obra = models.ForeignKey(
        Obra,
        on_delete=models.CASCADE
    )

    cantidad = models.PositiveIntegerField(default=1)

    agregado = models.DateTimeField(auto_now_add=True)

    def subtotal(self):
        return self.cantidad * self.obra.precio

    def __str__(self):
        return f"{self.cantidad} x {self.obra.nombre}"
