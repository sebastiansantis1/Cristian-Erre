from django.urls import path
from . import views

urlpatterns = [
    path('', views.panel_home, name='panel_home'),
    path('obra/editar/<int:obra_id>/', views.editar_obra, name='editar_obra'),
    path('obra/crear/', views.crear_obra, name='crear_obra'),
    path('obra/<int:obra_id>/destacada/', views.toggle_destacada, name='toggle_destacada'),
    path('obra/<int:obra_id>/mover/<str:direccion>/', views.mover_obra, name='mover_obra'),
    path('obra/<int:obra_id>/preview/', views.preview_obra, name='preview_obra'),
    path('obra/<int:obra_id>/agregar-imagen/', views.agregar_imagen_extra, name='agregar_imagen_extra'),
]
