from django.db import models
import datetime

class Post (models.Model):
    titulo = models.CharField(max_length= 50, null=False, blank=False )
    subtitulo = models.CharField(max_length=100, null=False,blank=False)
    cuerpo = models.TextField(null=False, blank=False)
    autor = models.CharField(max_length=50, null = False, blank= False)
    fecha = models.DateField(datetime.date.today)
    imagen = models.ImageField(upload_to= "posteos-imagen")