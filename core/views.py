from django.shortcuts import render
from cms.models import HomePageContent
from obras.models import Obra


def home(request):
    contenido_home = HomePageContent.get_solo()

    # Obtener obras destacadas publicadas y en stock
    obras_destacadas = Obra.objects.filter(
        estado="publicada",
        destacada=True,
        en_stock=True
    ).order_by('orden')[:6]  # limite para el carrusel

    context = {
        "contenido_home": contenido_home,
        "obras_destacadas": obras_destacadas,
    }

    return render(request, "core/home.html", context)
