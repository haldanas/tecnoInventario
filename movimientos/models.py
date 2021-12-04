from django.db import models

# Create your models here.

class Movimiento(models.Model):
    "modelo ORM Movimientos"
    SUMA = 'S'
    RESTA = 'R'
    OPERA = 'O'
    MOVIMIENTOS = [
        (SUMA, 'Suma'),
        (RESTA, 'Resta'),
        (OPERA, 'Opeara'),
    ]
    #ajuste, entrada y salida
    id= models.CharField(primary_key=True, max_length=50,db_column="m_codigo")
    nombre= models.TextField(max_length=50, blank=False,db_column="m_nombre")
    operador=models.CharField(max_length=5, blank=False,db_column="m_operador")
    tipo = models.CharField(
        max_length=2,
        choices=MOVIMIENTOS,
        default=OPERA,
        db_column="m_tipo"
    )
    creado = models.DateField(auto_now_add=True,db_column="m_creado")
    modificado = models.DateField(auto_now=True,db_column="m_modificado")
    
    def __str__(self) -> str: 
        return f'{self.id}'