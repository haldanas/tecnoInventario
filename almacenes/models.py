from django.db import models
from referencias.models import Referencia
# Create your models here.

class Almacen(models.Model):
    "modelo ORM almacenes"
          
    alm_codigo= models.AutoField(primary_key=True)
    
    alm_nombre = models.TextField(max_length=50, blank=False)
    alm_direccion= models.TextField(max_length=100, blank=False)
    alm_estado = models.TextChoices('ACTIVO','INACTIVO')
    alm_creado = models.DateField(auto_now_add=True)
    alm_modificado = models.DateField(auto_now=True)
    
    referencias = models.ManyToManyField(Referencia, through='Inventario') 

    def __str__(self) -> str: 
        return f'{self.alm_codigo}'
    
    
class Inventario(models.Model):
    alm_codigo = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    ref_codigo = models.ForeignKey(Referencia, on_delete=models.CASCADE)
    
    inv_cantidad = models.TextField(max_length=50, blank=False)
    inv_creado = models.DateField(auto_now_add=True)
    inv_modificado = models.DateField(auto_now=True)