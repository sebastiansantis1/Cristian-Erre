from django.contrib import admin
from .models import Categoria, Obra


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):

    list_display = ('id', 'nombre')
    search_fields = ('nombre',)


@admin.register(Obra)
class ObraAdmin(admin.ModelAdmin):

    list_display = ('id', 'nombre', 'categoria', 'precio', 'en_stock', 'fecha_creacion')
    list_filter = ('categoria', 'en_stock', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion_emocional', 'terminos_tecnicos')
    list_editable = ('en_stock',)
    readonly_fields = ('fecha_creacion',)
