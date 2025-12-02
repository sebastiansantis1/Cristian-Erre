from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from .models import HomePageContent
from .forms import HomePageContentForm


def es_admin(user):
    # Solo usuarios autenticados con rol ADMIN o superusuario
    if not user.is_authenticated:
        return False
    return user.is_superuser or getattr(user, "rol", None) == "ADMIN"


@user_passes_test(es_admin, login_url="/usuarios/login/")
def cms_home(request):
    contenido = HomePageContent.get_solo()

    if request.method == "POST":
        form = HomePageContentForm(request.POST, request.FILES, instance=contenido)
        if form.is_valid():
            form.save()
            messages.success(request, "Contenido de la página de inicio actualizado correctamente.")
            return redirect("cms_home")
        else:
            messages.error(request, "Por favor corrige los errores del formulario.")
    else:
        form = HomePageContentForm(instance=contenido)

    contexto = {
        "form": form,
        "contenido": contenido,
    }
    return render(request, "cms/cms_home.html", contexto)
