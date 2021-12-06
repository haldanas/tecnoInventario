from django import forms
from almacenes.models import Almacen, Inventario

class AlmacenForm(forms.Form):
    alm_nombre = forms.CharField(max_length=200, required=True)
    alm_direccion= forms.CharField(max_length=200, required=True)
    alm_estado = forms.CharField(max_length=200, required=True)

class InventarioForm(forms.Form):
    alm_codigo = forms.IntegerField(required=True)
    ref_codigo = forms.IntegerField(required=True)
    inv_cantidad = forms.IntegerField(required=True)
