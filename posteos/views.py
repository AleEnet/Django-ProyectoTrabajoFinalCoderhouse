from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import CreateUserForm, UserProfileForm,PasswordChangingForm,PostEditForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

def home(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request,"posteos/home.html", context)

def acercademi(request):
    return render(request, "acercademi.html")

def mostrar_post(request,post_id):
    post=Post.objects.get(pk = post_id)
    context = {"post":post}
    return render(request, "posteos/mostrar_post.html", context)


def register(request):
    form = CreateUserForm
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario creado exitosamente!")
            return redirect("login")
            
    context = {"form": form}
    return render(request,"register.html",context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.info(request,"Usuario o contraseña incorrectos")
            
    return render (request, "login.html")


def logoutuser(request):
    logout(request)
    return redirect('login')


@login_required
def agregar_post(request):
    return render (request, "posteos/agregar_post.html" )

@login_required
def agregar_post(request):
    if request.method == "POST":
        data = request.POST
        imagen = request.FILES.get("imagen")
        user = request.user

        nuevo_post = Post.objects.create(
            titulo = data["titulo"],
            subtitulo = data["subtitulo"],
            user = user,
            cuerpo = data["cuerpo"],
            fecha = data["fecha"],
            imagen = imagen
        )
        return redirect ("perfil_usuario")
    
    return render(request,"posteos/agregar_post.html")


@login_required
def editar_post(request,post_id):
    post = Post.objects.get(pk=post_id)
    form = PostEditForm(instance= post)
    context = {"post":post, "form": form}
    if request.method == "POST":
        form = PostEditForm(request.POST,request.FILES, instance= post)
        if form.is_valid():
            form.save()
            return redirect('perfil_usuario')


    return render (request, "posteos/editar_post.html",context)

@login_required
def eliminar_post(request,post_id):
    post = Post.objects.get(pk = post_id)
    post.delete()
    messages.success(request, f"{post.titulo} eliminado!")
    return redirect('perfil_usuario')






@login_required
def perfil_usuario (request):
    user = request.user
    posts = Post.objects.filter(user = user)
    context = {"posts":posts}   
          

    return render (request,"posteos/perfil_usuario.html",context)


class PasswordsChangeView (PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('passwordsuccess')

def PasswordSuccess(request):
    return render(request,"posteos/passwordsuccess.html")


def editar_perfil (request):
    userprofile = request.user.userprofile
    form = UserProfileForm(instance=userprofile)
    context = {"form":form}

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance= userprofile)
        if form.is_valid():
            form.save()
            

    return render (request,"posteos/editar_perfil.html",context)


def busqueda_post(request):
    if request.method == "POST":
        buscar = request.POST["busqueda"]
        post = Post.objects.filter(titulo__contains = buscar)
        context= {"buscar":buscar,"post":post}
        return render (request, 'posteos/busqueda_post.html', context)
    else:
        return render (request, "posteos/home.html")





# Create your views here.
