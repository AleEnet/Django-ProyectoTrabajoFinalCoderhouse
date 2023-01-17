from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mensaje
from .forms import MensajeForm
from django.contrib import messages
from django.contrib.auth.models import User


def enviar_mensaje(request):
    form = MensajeForm
    
    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje_nuevo = form.save(commit=False)
            mensaje_nuevo.de = request.user
            mensaje_nuevo.save()
            messages.success(request, "Mensaje enviado!")
            return redirect("mensajes_enviados")

    context = {"form":form}
    return render (request,"enviar_mensaje.html",context)


    
def mensajes_enviados(request):
    user = request.user
    mensajes= Mensaje.objects.filter(de= user )
    context = {"mensajes":mensajes}
    return render (request,"mensajes_enviados.html",context)

def mensajes_recibidos(request):
    user = request.user
    mensajes= Mensaje.objects.filter(para = user)
    context = {"mensajes":mensajes}
    return render (request, "mensajes_recibidos.html",context)

def mostrar_mensaje(request,mensaje_id):
    mensaje = Mensaje.objects.get(pk = mensaje_id)
    context = {"mensaje":mensaje}
    return render(request, "mostrar_mensaje.html",context)

def borrar_mensaje (request,mensaje_id):
    mensaje = Mensaje.objects.get(pk = mensaje_id)
    mensaje.delete()
    messages.success(request,'Mensaje eliminado!')
    return redirect('mensajes_enviados')
# Create your views here.
