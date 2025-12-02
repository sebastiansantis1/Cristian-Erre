from django import forms
from .models import HomePageContent


class HomePageContentForm(forms.ModelForm):
    class Meta:
        model = HomePageContent
        fields = [
            "titulo_principal",
            "subtitulo",
            "imagen_fondo",
            "texto_boton",
            "url_boton",
            "mostrar_boton",
            "instagram_url",
            "tiktok_url",
            "whatsapp_url",
            "email_contacto",
            "activo",
        ]
