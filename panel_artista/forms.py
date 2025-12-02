from django import forms
from obras.models import Obra, ObraImagen, Categoria


class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = [
            'nombre',
            'descripcion_emocional',
            'terminos_tecnicos',
            'tiempo_produccion',
            'precio',
            'categoria',
            'imagen_principal',
            'en_stock',
            'estado',
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'input'}),
            'descripcion_emocional': forms.Textarea(attrs={'class': 'input'}),
            'terminos_tecnicos': forms.Textarea(attrs={'class': 'input'}),
            'tiempo_produccion': forms.TextInput(attrs={'class': 'input'}),
            'precio': forms.NumberInput(attrs={'class': 'input'}),
            'categoria': forms.Select(attrs={'class': 'input'}),
            'imagen_principal': forms.FileInput(attrs={'class': 'input'}),
            'estado': forms.Select(attrs={'class': 'input'}),
        }


class ObraImagenForm(forms.ModelForm):
    class Meta:
        model = ObraImagen
        fields = ["imagen", "descripcion"]

        widgets = {
            "imagen": forms.FileInput(attrs={"class": "input"}),
            "descripcion": forms.TextInput(attrs={"class": "input"}),
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "input"}),
        }
