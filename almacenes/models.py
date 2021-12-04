from django.db import models
from referencias.models import Referencia

class Almacen(models.Model):
    "modelo ORM almacenes"
    id= models.AutoField(primary_key=True,db_column="a_codigo")
    
    nombre = models.TextField(max_length=50, blank=False,db_column="a_nombre")
    direccion= models.TextField(max_length=100, blank=False,db_column="a_direccion")    
    creado = models.DateField(auto_now_add=True,db_column="a_creado")
    modificado = models.DateField(auto_now=True,db_column="a_modificado")
    
    #through para nuevas tablas con atributos
    referencias = models.ManyToManyField(Referencia, through='inventario') 

    def __unicode__(self) -> str: 
        return self.id
    
class Inventario(models.Model):
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE,db_column="a_codigo")
    referencia = models.ForeignKey(Referencia, on_delete=models.CASCADE,db_column="r_codigo")
    
    cantidad = models.IntegerField(default=0,db_column="i_cantidad")
    creado = models.DateField(auto_now_add=True,db_column="i_creado")
    modificado = models.DateField(auto_now=True,db_column="i_modificado")