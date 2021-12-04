from django import forms

class PerfilForm(forms.Form):
    cargo = forms.CharField(max_length=200, required=True)
    