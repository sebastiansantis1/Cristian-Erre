from .models import Pedido, ItemPedido


def crear_pedido_desde_carrito(carrito):

    pedido = Pedido.objects.create(
        usuario=carrito.usuario,
        total=carrito.total()
    )

    for item in carrito.items.all():
        ItemPedido.objects.create(
            pedido=pedido,
            obra=item.obra,
            cantidad=item.cantidad,
            precio_unitario=item.obra.precio
        )

    # Vaciar carrito
    carrito.items.all().delete()

    return pedido
