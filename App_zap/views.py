from django.shortcuts import render

# Create your views here.


def inicio(self):
    
    return render(self, "inicio.html")

def zapatos(self):

    return render(self, "zapatos.html")

def accesorios(self):

    return render(self, "accesorios.html")

def proveedores(self):

    return render(self, "proveedores.html")

def sucursales(self):

    return render(self, "sucursales.html")


