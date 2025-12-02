from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import UsuarioRegistroForm


def registro(request):

    if request.method == 'POST':
        form = UsuarioRegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            # Logueamos al usuario recién creado
            login(request, usuario)
            return redirect('perfil')
    else:
        form = UsuarioRegistroForm()

    context = {
        'form': form,
    }
    return render(request, 'usuarios/registro.html', context)


@login_required
def perfil(request):

    usuario = request.user
    context = {
        'usuario': usuario,
    }
    return render(request, 'usuarios/perfil.html', context)
