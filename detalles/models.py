from django.db import models
from movimientos.models import Movimiento
from usuarios.models import Perfil
from almacenes.models import Almacen
from referencias.models import Referencia
# Create your models here.

class Detalle(models.Model):
    "modelo ORM Detaill o Detalle"
    
    det_codigo = models.AutoField(primary_key=True)
    
    alm_codigo= models.ForeignKey(Almacen, on_delete=models.PROTECT)
    perfil = models.ForeignKey(Perfil, on_delete=models.PROTECT)
    mov_codigo = models.ForeignKey(Movimiento, on_delete=models.PROTECT)
    
    #movimeinto
    det_cantidad = models.CharField(max_length=100, blank=False)
    det_estado = models.TextChoices(
        'Procesado','Reversado',
    )
    det_observacion = models.TextField(max_length=200, blank=True)
    det_creado = models.DateField(auto_now_add=True)
    det_modificado = models.DateField(auto_now=True)
    registros = models.ManyToManyField(Referencia, through='Registro') 
    
    def __str__(self) -> str: 
        return f'{self.det_codigo}'

# Create your models here.
class Registro(models.Model):
    "modelo ORM registros"
    
    det_codigo=models.ForeignKey(Detalle, on_delete=models.CASCADE)
    ref_codigo=models.ForeignKey(Referencia, on_delete=models.CASCADE)
    
    reg_mac= models.TextField(max_length=100)
    reg_sn= models.TextField(max_length=100)
    u_creado = models.DateField(auto_now_add=True)
    u_modificado = models.DateField(auto_now=True)