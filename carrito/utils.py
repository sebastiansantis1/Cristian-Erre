from .models import Carrito, ItemCarrito


def obtener_carrito(request):

    # Si el usuario está autenticado → carrito vinculado a su cuenta
    if request.user.is_authenticated:
        carrito, creado = Carrito.objects.get_or_create(usuario=request.user)
        return carrito

    # Si es anónimo vamos a usar su session_key
    if not request.session.session_key:
        request.session.save()

    session_key = request.session.session_key

    carrito, creado = Carrito.objects.get_or_create(session_key=session_key)
    return carrito


def agregar_item(carrito, obra, cantidad=1):

    item, creado = ItemCarrito.objects.get_or_create(
        carrito=carrito,
        obra=obra,
    )
    if not creado:
        item.cantidad += cantidad
    item.save()
    return item


def eliminar_item(item_id):
    ItemCarrito.objects.filter(id=item_id).delete()


def actualizar_cantidad(item_id, nueva_cantidad):
    item = ItemCarrito.objects.get(id=item_id)
    item.cantidad = nueva_cantidad
    item.save()
