from django.db import models
from django.contrib.auth.models import User

from usuarios.models import Perfil
from almacenes.models import Almacen
# Create your models here.

class Detalle(models.Model):
    "modelo ORM Detaill o Detalle"
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    #perfil = models.ForeignKey('usuarios.perfil', on_delete=models.PROTECT) 
    perfil = models.ForeignKey(Perfil, on_delete=models.PROTECT) 
    alm_codigo =models.ForeignKey(Almacen, on_delete=models.PROTECT) 
    det_codigo = models.CharField(max_length=100, blank=False)
    
    # XXXX 
    #codifo_detalle
    #movimeinto
    det_cantidad = models.CharField(max_length=100, blank=False)
    det_estado = models.TextChoices(
        'Procesado','Reversado',
    )
    det_observacion = models.TextField(max_length=200, blank=True)
    det_creado = models.DateField(auto_now_add=True)
    det_modificado = models.DateField(auto_now=True)
    
    def __str__(self) -> str: 
        pass
        #return f'{self.title} by @{self.usuario.username}'