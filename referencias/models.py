from django.db import models
# Create your models here.

class Referencia(models.Model):
    "modelo ORM referencias"
    
    ref_codigo = models.AutoField(primary_key=True)
    
    ref_marca = models.TextField(max_length=50)
    ref_nombre = models.TextField(max_length=50)
    ref_observacion = models.TextField(max_length=200, blank=True)
    ref_creado = models.DateField(auto_now_add=True)
    ref_modificado = models.DateField(auto_now=True)
    
    def __str__(self) -> str: 
        return f'{self.ref_codigo}'