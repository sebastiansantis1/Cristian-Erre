from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from .forms import UsuarioRegistroForm, UsuarioLoginForm


# ---------------------------------------------------
# REGISTRO DE USUARIO
# ---------------------------------------------------
def registro_view(request):

    if request.method == 'POST':
        form = UsuarioRegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  # Logueo automático
            return redirect('perfil')
    else:
        form = UsuarioRegistroForm()

    return render(request, 'usuarios/registro.html', {'form': form})


# ---------------------------------------------------
# LOGIN
# ---------------------------------------------------
def login_view(request):

    if request.method == 'POST':
        form = UsuarioLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('perfil')
        # Si falla, se mostrará error dentro del mismo formulario

    else:
        form = UsuarioLoginForm()

    return render(request, 'usuarios/login.html', {'form': form})


# ---------------------------------------------------
# PERFIL (Protegido)
# ---------------------------------------------------
@login_required
def perfil_view(request):

    usuario = request.user
    return render(request, 'usuarios/perfil.html', {'usuario': usuario})


# ---------------------------------------------------
# LOGOUT
# ---------------------------------------------------
def logout_view(request):
    
    logout(request)
    return render(request, 'usuarios/logout.html')
