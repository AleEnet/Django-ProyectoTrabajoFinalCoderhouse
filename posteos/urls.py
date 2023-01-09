from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name = "home"),
    path("descipcion_autor/",descripcion_autor, name="descripcion_autor"),
    path("detalle_posteo/",detalle_posteo, name = "detalle_posteo"),
    path("register/",register, name = "register"),
    path("login/",loginPage, name="login"),
]