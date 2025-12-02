from django.urls import path
from .views import cms_home

urlpatterns = [
    path("", cms_home, name="cms_home"),
]
