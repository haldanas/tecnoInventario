from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Perfil(models.Model):
    "modelo ORM perfil"
    
    usuario = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, db_column="p_usuario")
    cargo = models.TextField(max_length=200, blank=False, db_column="p_cargo")
    
    creado = models.DateField(auto_now_add=True, db_column="p_creado")
    modificado = models.DateField(auto_now=True,db_column="p_modificado")
    
    def __str__(self) -> str: 
        return self.usuario.username