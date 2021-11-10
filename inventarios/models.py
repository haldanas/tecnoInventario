from django.db import models
from referencias.models import Referencia
from almacenes.models import Almacen

# Create your models here.

class Inventario(models.Model):
    "modelo ORM inventarios"
    
    #usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    ref_codigo = models.ForeignKey(Referencia, on_delete=models.PROTECT)
    alm_codigo= models.ForeignKey(Almacen, on_delete=models.PROTECT)
    
    inv_cantidad = models.TextField(max_length=50, blank=False)
    
    #inv_estado = models.TextChoices('ACTIVO','INACTIVO')    
    inv_creado = models.DateField(auto_now_add=True)
    inv_modificado = models.DateField(auto_now=True)
    
    
    def __str__(self) -> str: 
        return f'{self.ref_codigo},{self.alm_codigo}'