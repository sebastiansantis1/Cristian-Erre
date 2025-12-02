from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

from obras.models import Obra, ObraImagen, Categoria
from .forms import ObraForm, ObraImagenForm, CategoriaForm


# -------------------------------------------------------
# Validación: solo el artista (admin) puede entrar al panel
# -------------------------------------------------------

def es_admin(user):
    return user.is_authenticated and user.rol == "admin"


# -------------------------------------------------------
# DASHBOARD PRINCIPAL DEL PANEL
# -------------------------------------------------------

@login_required
@user_passes_test(es_admin)
def panel_home(request):

    obras = Obra.objects.all().order_by('-destacada', 'orden', '-fecha_creacion')

    return render(request, "panel_artista/panel_home.html", {
        "obras": obras
    })


# -------------------------------------------------------
# CREAR NUEVA OBRA
# -------------------------------------------------------

@login_required
@user_passes_test(es_admin)
def crear_obra(request):
    if request.method == "POST":
        form = ObraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("panel_home")
    else:
        form = ObraForm()

    return render(request, "panel_artista/crear_obra.html", {
        "form": form
    })


# -------------------------------------------------------
# EDITAR OBRA EXISTENTE
# -------------------------------------------------------

@login_required
@user_passes_test(es_admin)
def editar_obra(request, obra_id):
    obra = get_object_or_404(Obra, id=obra_id)

    # Manejar formulario principal de obra
    if request.method == "POST":
        form = ObraForm(request.POST, request.FILES, instance=obra)
        if form.is_valid():
            form.save()
            return redirect("panel_home")
    else:
        form = ObraForm(instance=obra)

    # Galería de imágenes extra existentes
    imagenes_extra = obra.imagenes_extra.all()

    return render(request, "panel_artista/editar_obra.html", {
        "form": form,
        "obra": obra,
        "imagenes_extra": imagenes_extra,
    })


# -------------------------------------------------------
# AGREGAR IMAGEN ADICIONAL A LA GALERÍA
# -------------------------------------------------------

@login_required
@user_passes_test(es_admin)
def agregar_imagen_extra(request, obra_id):
    obra = get_object_or_404(Obra, id=obra_id)

    if request.method == "POST":
        form = ObraImagenForm(request.POST, request.FILES)
        if form.is_valid():
            imagen = form.save(commit=False)
            imagen.obra = obra
            imagen.save()
            return redirect("editar_obra", obra_id=obra.id)
    else:
        form = ObraImagenForm()

    return render(request, "panel_artista/agregar_imagen_extra.html", {
        "form": form,
        "obra": obra
    })


# -------------------------------------------------------
# PREVIEW DE OBRA (SOLO BOCETO, NO PUBLICADO)
# -------------------------------------------------------

@login_required
@user_passes_test(es_admin)
def preview_obra(request, obra_id):
    obra = get_object_or_404(Obra, id=obra_id)

    return render(request, "panel_artista/preview_obra.html", {
        "obra": obra
    })


# -------------------------------------------------------
# DESTACAR O DESMARCAR OBRA
# -------------------------------------------------------

@login_required
@user_passes_test(es_admin)
def toggle_destacada(request, obra_id):
    obra = get_object_or_404(Obra, id=obra_id)
    obra.destacada = not obra.destacada
    obra.save()
    return redirect("panel_home")


# -------------------------------------------------------
# REORDENAR OBRAS - MOVER ARRIBA / ABAJO
# -------------------------------------------------------

@login_required
@user_passes_test(es_admin)
def mover_obra(request, obra_id, direccion):

    obra = get_object_or_404(Obra, id=obra_id)

    if direccion == "up":
        obra.orden -= 1
    elif direccion == "down":
        obra.orden += 1

    obra.save()
    return redirect("panel_home")


# -------------------------------------------------------
# CRUD DE CATEGORÍAS
# -------------------------------------------------------

@login_required
@user_passes_test(es_admin)
def categorias(request):
    lista = Categoria.objects.all().order_by("nombre")

    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categorias")
    else:
        form = CategoriaForm()

    return render(request, "panel_artista/categorias.html", {
        "categorias": lista,
        "form": form
    })


@login_required
@user_passes_test(es_admin)
def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect("categorias")
    else:
        form = CategoriaForm(instance=categoria)

    return render(request, "panel_artista/editar_categoria.html", {
        "form": form,
        "categoria": categoria
    })


@login_required
@user_passes_test(es_admin)
def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    categoria.delete()
    return redirect("categorias")
