from django.db import models

# -----------------------------------
# CATEGORÍAS
# -----------------------------------

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


# -----------------------------------
# OBRAS
# -----------------------------------

ESTADOS_OBRA = (
    ('borrador', 'Borrador (solo visible en el Panel)'),
    ('publicada', 'Publicada (visible en el catálogo)'),
)

class Obra(models.Model):

    # --- Campos principales ---
    nombre = models.CharField(max_length=200)
    descripcion_emocional = models.TextField(blank=True)
    terminos_tecnicos = models.TextField(blank=True)
    tiempo_produccion = models.CharField(max_length=200, blank=True)

    precio = models.DecimalField(max_digits=10, decimal_places=2)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="obras"
    )

    imagen_principal = models.ImageField(
        upload_to="obras/",
        null=True,
        blank=True
    )

    # --- Control de visibilidad ---
    en_stock = models.BooleanField(default=True)

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS_OBRA,
        default='publicada'
    )

    destacada = models.BooleanField(default=False)

    orden = models.PositiveIntegerField(
        default=0,
        help_text="Permite ordenar obras manualmente desde el panel."
    )

    # --- Control y metadata ---
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    # Mostrar siempre primero destacadas y luego por orden
    class Meta:
        ordering = ['-destacada', 'orden', '-fecha_creacion']


# -----------------------------------
# GALERÍA DE IMÁGENES EXTRA
# -----------------------------------

class ObraImagen(models.Model):
    obra = models.ForeignKey(
        Obra,
        on_delete=models.CASCADE,
        related_name="imagenes_extra"
    )
    imagen = models.ImageField(upload_to="galeria/")
    descripcion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Imagen extra de {self.obra.nombre}"

