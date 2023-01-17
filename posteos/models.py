from django.db import models
from django.contrib.auth.models import User
import datetime
from django.dispatch import receiver 
from django.db.models.signals import post_save 

class Post (models.Model):
    titulo = models.CharField(max_length= 50, null=False, blank=False )
    subtitulo = models.CharField(max_length=100, null=False,blank=False)
    cuerpo = models.TextField(null=False, blank=False)
    user = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to= "posteos-imagen")

    def __str__(self):
        return f"{self.titulo}, {self.user}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, null= False, on_delete = models.CASCADE)
    nombre_usuario = models.CharField(default = 'username', max_length=50, null = True, blank=True)
    email = models.EmailField(null = True, blank=True)
    fecha_nacimiento = models.DateField(null = True, blank=True)
    imagen = models.ImageField(upload_to = "usuarios-imagen", null =True, blank= True, default="user_defoult.png")
    fecha_creado = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User) 
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()

