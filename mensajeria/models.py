from django.db import models
from django.contrib.auth.models import User
from posteos.models import UserProfile



class Mensaje(models.Model):
    de =  models.CharField(max_length=150, null = True, blank=True)
    para = models.ForeignKey(User, on_delete = models.CASCADE)
    titulo = models.CharField(max_length=150, null = True, blank=True)
    asunto = models.CharField(max_length=50, null = True, blank=True)
    cuerpo =models.TextField(null = True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.asunto