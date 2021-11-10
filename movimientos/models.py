from django.db import models

# Create your models here.

class Movimiento(models.Model):
    "modelo ORM Movimientos"
    
    mov_code= models.CharField(max_length=50, blank=False)   
    
    mov_tipo=models.TextChoices('SUMA','RESTA','OPERA')
    mov_nombre= models.TextField(max_length=50, blank=False)
    mov_operador=models.CharField(max_length=5, blank=False)
     
    mov_creado = models.DateField(auto_now_add=True)
    mov_modificado = models.DateField(auto_now=True)
    
    def __str__(self) -> str: 
        pass
        #return f'{self.ref_codigo},{self.alm_codigo}'