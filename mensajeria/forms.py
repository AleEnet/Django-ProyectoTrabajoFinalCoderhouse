from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Mensaje

class MensajeForm(ModelForm):
    class Meta:
        model = Mensaje
        fields = ("para","titulo","asunto","cuerpo")
        widgets = {
            "para": forms.Select(attrs={"class":"form-control"}),
            "titulo": forms.TextInput(attrs={"class":"form-control"}),
            "asunto":forms.TextInput(attrs={"class":"form-control"}),
            "cuerpo":forms.TextInput(attrs={"class":"form-control"})
                                 
        }
