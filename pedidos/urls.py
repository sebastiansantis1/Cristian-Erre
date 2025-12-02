from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('confirmar/', views.confirmar_pedido, name='confirmar_pedido'),
    path('confirmado/<int:pedido_id>/', views.pedido_confirmado, name='pedido_confirmado'),
    path('mis-pedidos/', views.mis_pedidos, name='mis_pedidos'),
]
