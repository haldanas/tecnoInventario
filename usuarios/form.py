from typing import Text
from django import forms
from django.forms.fields import CharField

class PerfilForm(forms.Form):
    cargo = forms.CharField(max_length=200, required=True)