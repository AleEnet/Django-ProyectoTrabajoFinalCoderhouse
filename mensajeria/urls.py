from django.urls import path
from .views import *

urlpatterns = [
    path("enviar_mensaje/", enviar_mensaje, name = "enviar_mensaje"),
    path("recibidos/",mensajes_recibidos,name = "mensajes_recibidos"),
    path("enviados/",mensajes_enviados,name = "mensajes_enviados"),
    path("mostrar_mensaje/<mensaje_id>",mostrar_mensaje,name="mostrar_mensaje"),
    path("borrar_mensaje/<mensaje_id>",borrar_mensaje, name = "borrar_mensaje"),]