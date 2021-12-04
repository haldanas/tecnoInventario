from django.db import models
from movimientos.models import Movimiento
from usuarios.models import Perfil
from almacenes.models import Almacen
from referencias.models import Referencia
# Create your models here.

class Detalle(models.Model):
    id = models.AutoField(primary_key=True,db_column="d_codigo")
    
    almacen = models.ForeignKey(Almacen, on_delete=models.PROTECT,db_column="a_codigo")
    perfil = models.ForeignKey(Perfil, on_delete=models.PROTECT,db_column="p_codigo")
    movimiento = models.ForeignKey(Movimiento, on_delete=models.PROTECT,db_column="m_codigo")
    
    cantidad = models.CharField(max_length=100, blank=False,db_column="d_cantidad")
    observacion = models.TextField(max_length=200, blank=True,db_column="d_observacion")
    creado = models.DateField(auto_now_add=True,db_column="d_creado")
    modificado = models.DateField(auto_now=True,db_column="d_modificado")
    
    registros = models.ManyToManyField(Referencia, through='registro')
    
    def __str__(self) -> str: 
        return self.id

# Create your models here.
class Registro(models.Model):
    "modelo ORM registros"
    
    detalle= models.ForeignKey(Detalle, on_delete=models.CASCADE, db_column="d_codigo")
    referencia= models.ForeignKey(Referencia, on_delete=models.CASCADE,db_column="r_codigo")
    
    mac= models.TextField(max_length=100,db_column="reg_mac")
    sn= models.TextField(max_length=100,db_column="reg_sn")
    creado = models.DateField(auto_now_add=True,db_column="reg_creado")
    modificado = models.DateField(auto_now=True,db_column="reg_modificado")