from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    perfil = models.ForeignKey('usuarios.Perfil', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='posts/fotos')
    adicionado = models.DateField(auto_now_add=True)
    modificado = models.DateField(auto_now=True)

    def __str__(self):
        return '{} by @{}'.format(self.titulo, self.usuario)
