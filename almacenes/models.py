from django.db import models
from django.db.models.enums import Choices
# Create your models here.

class Almacen(models.Model):
    "modelo ORM almacenes"
    
    #usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    alm_codigo= models.CharField(max_length=20, null=False)
    
    alm_nombre = models.TextField(max_length=50, blank=False)
    alm_direccion= models.TextField(max_length=100, blank=False)
    alm_estado = models.TextChoices('ACTIVO','INACTIVO')
    
    alm_creado = models.DateField(auto_now_add=True)
    alm_modificado = models.DateField(auto_now=True)
    
    
    def __str__(self) -> str: 
        return f'{self.alm_codigo}'