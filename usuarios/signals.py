from django.apps import apps
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver

User = get_user_model()

@receiver(post_migrate)
def crear_grupos_por_defecto(sender, **kwargs):
    if sender.name != "usuarios":
        return

    # --- Grupo Administradores ---
    admin_group, _ = Group.objects.get_or_create(name="Administradores")
    admin_perms = Permission.objects.filter(codename__in=[
        'add_obra', 'change_obra', 'delete_obra', 'view_obra',
        'add_categoria', 'change_categoria', 'delete_categoria', 'view_categoria',
        'add_pedido', 'change_pedido', 'delete_pedido', 'view_pedido',
        'add_usuario', 'change_usuario', 'delete_usuario', 'view_usuario'
    ])
    admin_group.permissions.set(admin_perms)

    # --- Grupo Clientes ---
    clientes_group, _ = Group.objects.get_or_create(name="Clientes")
    clientes_perms = Permission.objects.filter(codename__in=[
        'view_obra', 'view_categoria', 'add_pedido', 'view_pedido'
    ])
    clientes_group.permissions.set(clientes_perms)

#Esto detecta el rol al crear el usuario y lo agrega automáticamente al grupo correspondiente

@receiver(post_save, sender=User)
def asignar_grupo_por_rol(sender, instance, created, **kwargs):
    if created:
        rol = getattr(instance, "rol", None)

        if rol == "ADMIN":
            grupo = Group.objects.get(name="Administradores")
            instance.groups.add(grupo)

        elif rol == "CLIENTE":
            grupo = Group.objects.get(name="Clientes")
            instance.groups.add(grupo)

