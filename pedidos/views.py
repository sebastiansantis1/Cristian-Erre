from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from carrito.utils import obtener_carrito
from pedidos.utils import crear_pedido_desde_carrito
from .models import Pedido


@login_required
def checkout(request):

    carrito = obtener_carrito(request)
    items = carrito.items.all()

    if not items:
        return redirect('ver_carrito')

    return render(request, 'pedidos/checkout.html', {
        'carrito': carrito,
        'items': items,
        'total': carrito.total(),
    })


@login_required
def confirmar_pedido(request):

    carrito = obtener_carrito(request)
    items = carrito.items.all()

    if not items:
        return redirect('ver_carrito')

    pedido = crear_pedido_desde_carrito(carrito)

    return redirect('pedido_confirmado', pedido_id=pedido.id)


@login_required
def pedido_confirmado(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id, usuario=request.user)

    return render(request, 'pedidos/pedido_confirmado.html', {
        'pedido': pedido
    })


@login_required
def mis_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user).order_by('-fecha')

    return render(request, 'pedidos/mis_pedidos.html', {
        'pedidos': pedidos
    })
