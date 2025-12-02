from django.apps import apps
from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver


@receiver(post_migrate)
def crear_grupos_por_defecto(sender, **kwargs):

    # Nos aseguramos de que esto se ejecute solo cuando migra la app 'usuarios'
    if sender.name != "usuarios":
        return

    Group.objects.get_or_create(name="Administradores")
    Group.objects.get_or_create(name="Clientes")
