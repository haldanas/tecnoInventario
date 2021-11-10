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
    mov_codigo= models.CharField(primary_key=True, max_length=50)
    mov_nombre= models.TextField(max_length=50, blank=False)
    mov_operador=models.CharField(max_length=5, blank=False)
    mov_tipo = models.CharField(
        max_length=2,
        choices=MOVIMIENTOS,
        default=OPERA,
    )
    mov_creado = models.DateField(auto_now_add=True)
    mov_modificado = models.DateField(auto_now=True)
    
    def __str__(self) -> str: 
        return f'{self.mov_codigo}'