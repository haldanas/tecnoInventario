from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Perfil(models.Model):
    "modelo ORM perfil"
    
    usuario = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    cargo = models.TextField(max_length=200, blank=False)
    
    u_creado = models.DateField(auto_now_add=True)
    u_modificado = models.DateField(auto_now=True)
    
    def __str__(self) -> str: 
        return self.usuario.username