from django.db import models
from django.conf import settings
from obras.models import Obra


class Pedido(models.Model):

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='pedidos'
    )

    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    ESTADOS = (
        ('PENDIENTE', 'Pendiente de pago'),
        ('PAGADO', 'Pagado'),
        ('ENVIADO', 'Enviado'),
        ('COMPLETADO', 'Completado'),
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='PENDIENTE'
    )

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username}"



class ItemPedido(models.Model):

    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name='items'
    )

    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.cantidad * self.precio_unitario

    def __str__(self):
        return f"{self.cantidad} x {self.obra.nombre}"
