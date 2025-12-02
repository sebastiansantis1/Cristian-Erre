from django.db import models


class HomePageContent(models.Model):
    titulo_principal = models.CharField(
        max_length=150,
        verbose_name="Título principal"
    )
    subtitulo = models.TextField(
        blank=True,
        verbose_name="Subtítulo / descripción"
    )
    imagen_fondo = models.ImageField(
        upload_to="cms/hero/",
        blank=True,
        null=True,
        verbose_name="Imagen de fondo del hero"
    )
    texto_boton = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Texto del botón principal"
    )
    url_boton = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="URL del botón principal"
    )
    mostrar_boton = models.BooleanField(
        default=True,
        verbose_name="Mostrar botón principal"
    )

    instagram_url = models.URLField(
        blank=True,
        verbose_name="Instagram"
    )
    tiktok_url = models.URLField(
        blank=True,
        verbose_name="TikTok"
    )
    whatsapp_url = models.URLField(
        blank=True,
        verbose_name="WhatsApp"
    )
    email_contacto = models.EmailField(
        blank=True,
        verbose_name="Email de contacto"
    )

    activo = models.BooleanField(default=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contenido de la página de inicio"
        verbose_name_plural = "Contenido de la página de inicio"

    def __str__(self):
        return "Contenido Home"

    def save(self, *args, **kwargs):
        # Forzar que siempre exista solo un registro (pk=1)
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_solo(cls):
        # Devuelve siempre el único registro, creándolo con valores por defecto si no existe
        obj, created = cls.objects.get_or_create(
            pk=1,
            defaults={
                "titulo_principal": "Galería digital de alto nivel.",
                "subtitulo": (
                    "Obras cuidadosamente diseñadas, con enfoque en detalle, "
                    "emoción y técnica. Explora el catálogo, arma tu colección "
                    "y gestiona todo desde una experiencia limpia y elegante."
                ),
                "texto_boton": "Explorar catálogo",
                "url_boton": "/obras/",
                "mostrar_boton": True,
                "activo": True,
            },
        )
        return obj
