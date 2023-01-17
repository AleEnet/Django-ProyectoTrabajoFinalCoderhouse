from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home, name = "home"),
    path("register/",register, name = "register"),
    path("login/",loginPage, name="login"),
    path("logout/",logoutuser, name = "logout"),
    path("agregar_post/", agregar_post, name= "agregar_post"),
    path("eliminar_post/<post_id>",eliminar_post, name = "eliminar_post"),
    path("mostar_post/<post_id>",mostrar_post,name="mostar_post"),
    path("editar_post/<post_id>",editar_post,name="editar_post"),
    path("busqueda_post/",busqueda_post,name = "busqueda_post"),
    path("perfil_usuario/",perfil_usuario, name = "perfil_usuario"),
    path("password/",PasswordsChangeView.as_view(template_name = 'posteos/password.html'), name= "password"),
    path("passwordsuccess/", PasswordSuccess,name = "passwordsuccess"),
    path("editar_perfil/",editar_perfil,name="editar_perfil"),
    path("acercademi/",acercademi,name="acercademi"),
    
]