from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Perfil(models.Model):
    

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True)
    biografia = models.TextField(blank=True)
    telefono = models.CharField(max_length=12, blank=True)
    imagen = models.ImageField(upload_to='usuarios/imagenes', blank=True, null=True)
    adicionado = models.DateField(auto_now_add=True)
    modificado = models.DateField(auto_now=True)

    def __str__(self):
        return self.usuario.username