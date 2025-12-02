from django.contrib.auth.decorators import user_passes_test

def admin_required(view_func):
    return user_passes_test(
        lambda u: u.is_superuser or u.groups.filter(name="Administradores").exists(),
        login_url="/usuarios/login/"
    )(view_func)