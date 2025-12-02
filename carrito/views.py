from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from obras.models import Obra
from .utils import obtener_carrito, agregar_item, eliminar_item, actualizar_cantidad
from .models import ItemCarrito


def ver_carrito(request):
    carrito = obtener_carrito(request)
    items = carrito.items.all()

    context = {
        'carrito': carrito,
        'items': items,
        'total': carrito.total()
    }
    return render(request, 'carrito/carrito.html', context)


def agregar_al_carrito(request, obra_id):
    obra = get_object_or_404(Obra, id=obra_id)
    carrito = obtener_carrito(request)

    agregar_item(carrito, obra)
    return redirect('ver_carrito')


def eliminar_del_carrito(request, item_id):
    eliminar_item(item_id)
    return redirect('ver_carrito')


def actualizar_item(request, item_id):
    if request.method == 'POST':
        nueva_cantidad = int(request.POST.get('cantidad'))
        actualizar_cantidad(item_id, nueva_cantidad)
    return redirect('ver_carrito')
