from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario


class UsuarioRegistroForm(UserCreationForm):

    class Meta:
        model = Usuario
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'rol',
            'password1',
            'password2',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email', '').lower()
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un usuario registrado con este correo.")
        return email


class UsuarioLoginForm(AuthenticationForm):
    username = forms.CharField(label='Nombre de usuario')
