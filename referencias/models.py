from django.db import models
# Create your models here.

class Referencia(models.Model):
    "modelo ORM referencias"
    
    id = models.AutoField(primary_key=True,db_column="r_codigo")
    nombre = models.TextField(max_length=50,db_column="r_nombre")
    marca = models.TextField(max_length=50,db_column="r_marca")
    observacion = models.TextField(max_length=200, blank=True,db_column="r_observacion")
    creado = models.DateField(auto_now_add=True,db_column="r_creado")
    modificado = models.DateField(auto_now=True,db_column="r_modificado")
    
    def __unicode__(self) -> str: 
        return self.id