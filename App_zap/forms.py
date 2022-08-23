

from django import forms


class AccesorioFormulario(forms.Form):

    modelo = forms.CharField(max_length=50)
    color = forms.CharField(max_length=50)
    talla = forms.IntegerField()
    precio = forms.IntegerField()

class ZapatoFormulario(forms.Form):

    modelo = forms.CharField(max_length=50)
    color = forms.CharField(max_length=50)
    talla = forms.IntegerField()
    precio = forms.IntegerField()


class SucursalFormulario(forms.Form):
    num_Sucursal = forms.IntegerField()
    nombre_sucursal = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=50)

class ProveedorFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    fecha_de_afiliacion = forms.DateField()


