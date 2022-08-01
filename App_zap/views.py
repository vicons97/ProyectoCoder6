
from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from App_zap.forms import AccesorioFormulario

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


   # def accesorioFormulario(request):

   #     if request.method == 'POST':
   #         accesorios = Accesorios(modelo = request.POST['modelo'], color = request.POST['color'], talla = request.POST['talla'], precio=request.POST['precio'])

   #        accesorios.save()

   #         return render(request, 'inicio.html')


   #    return render(request, "accesorioFormulario.html")


def accesorioFormulario(request):

    if request.method == 'POST':
    
        miFormulario = AccesorioFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            accesorios = Accesorios(modelo = data['modelo'], color = data['color'], talla = data['talla'], precio=data['precio'])
            accesorios.save()

            return render(request, 'inicio.html')

    else:

        miFormulario = AccesorioFormulario()  

    return render(request, "accesorioFormulario.html", {"miFormulario": miFormulario})



def busquedaModelo(request):

    return render(request, 'busquedaModelo.html')

def buscar(request):

    if request.GET["modelo"]:

        modelo = request.GET["modelo"]

        talla = Accesorios.objects.filter(modelo__icontains=modelo)



        return render(request, "resultadoBusqueda.html", {"modelo":modelo, "talla":talla})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)



   



