from django.shortcuts import render, get_object_or_404
from .models import Obra, Categoria


# ---------------------------------------------------------
# LISTA DE OBRAS (CATÁLOGO PÚBLICO)
# ---------------------------------------------------------

def catalogo(request):

    obras = Obra.objects.filter(
        estado="publicada",
        en_stock=True
    ).order_by(
        '-destacada',
        'orden',
        '-fecha_creacion'
    )

    categorias = Categoria.objects.all().order_by("nombre")

    return render(request, "obras/lista_obras.html", {
        "obras": obras,
        "categorias": categorias,
    })


# ---------------------------------------------------------
# DETALLE DE OBRA (PÚBLICO)
# ---------------------------------------------------------

def detalle_obra(request, obra_id):

    obra = get_object_or_404(
        Obra,
        id=obra_id,
        estado="publicada"
    )

    imagenes_extra = obra.imagenes_extra.all()

    return render(request, "obras/detalle_obra.html", {
        "obra": obra,
        "imagenes_extra": imagenes_extra,
    })
