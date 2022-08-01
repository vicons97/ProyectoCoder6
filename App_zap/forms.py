

from django import forms


class AccesorioFormulario(forms.Form):

    modelo = forms.CharField()
    color = forms.CharField()
    talla = forms.IntegerField()
    precio = forms.IntegerField()

    

