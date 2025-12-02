from django.contrib import admin
from .models import HomePageContent


@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ["titulo_principal", "activo", "actualizado_en"]
    readonly_fields = ["actualizado_en"]

    def has_add_permission(self, request):
        # Solo permitir un registro en el admin
        if HomePageContent.objects.exists():
            return False
        return super().has_add_permission(request)
