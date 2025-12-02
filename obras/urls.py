from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('<int:obra_id>/', views.detalle_obra, name='detalle_obra'),
]
