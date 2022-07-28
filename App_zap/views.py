from django.shortcuts import render

from App_zap.models import Accesorios, Zapatos

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


def zapato(self, modelo, talla, color, precio):

    zapato = Zapatos(modelo = modelo, talla = talla, color = color, precio = precio)
    zapato.save()

    return render(self, "zapato.html", {'zapato': zapato})


def lista_zapatos(self):

    lista = Zapatos.objects.all()

    return render(self, "lista_zapatos.html", {'lista_zapatos': lista})


def accesorioFormulario(request):

    if request.method == 'POST':
        accesorios = Accesorios(modelo = request.POST['modelo'], color = request.POST['color'], talla = request.POST['talla'], precio=request.POST['precio'])

        accesorios.save()

        return render(request, 'inicio.html')


    return render(request, "accesorioFormulario.html")


    