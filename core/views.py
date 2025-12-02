from django.shortcuts import render
from cms.models import HomePageContent


def home(request):
    contenido_home = HomePageContent.get_solo()
    return render(request, "core/home.html", {"contenido_home": contenido_home})
