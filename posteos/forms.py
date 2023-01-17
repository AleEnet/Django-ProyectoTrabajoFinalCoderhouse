from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, Post

class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ["titulo","subtitulo","cuerpo","imagen"]
        widgets = {
            "titulo": forms.TextInput(attrs={"class":"form-control"}),
            "subtitulo": forms.TextInput(attrs={"class":"form-control"}),
            "cuerpo":forms.TextInput(attrs={"class":"form-control"}),
                           
        }    







class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1","password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class":"form-control"}),
            "password1":forms.PasswordInput(attrs={"class":"form-control"}),
            "password2":forms.PasswordInput(attrs={"class":"form-control"}),                      
        }

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ("email","fecha_nacimiento","imagen")
        widgets = {
            
            "email": forms.EmailInput(attrs={"class":"form-control"}),
            "fecha_nacimiento":forms.DateTimeInput(attrs={"class":"form-control"}),                      
        }

class PasswordChangingForm(PasswordChangeForm):
    old_password=forms.CharField(label="Contraseña anterior", widget= forms.PasswordInput (attrs={"class":"form-control",type:"password"}))
    new_password1=forms.CharField(label="Nueva contraseña ", max_length= 100, widget= forms.PasswordInput (attrs={"class":"form-control",type:"password"}))
    new_password2=forms.CharField(label="Repita la nueva contraseña ",max_length= 100, widget= forms.PasswordInput (attrs={"class":"form-control",type:"password"}))
    class Meta:
        model= User
        fields = ("old_password","new_password1","new_password2")

        


