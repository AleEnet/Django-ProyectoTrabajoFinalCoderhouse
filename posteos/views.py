from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request,"posteos/home.html")

def descripcion_autor(request):
    return render(request, "posteos/descripcion_autor.html")

def detalle_posteo(request):
    return render(request, "posteos/detalle_posteo.html")


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


# Create your views here.
