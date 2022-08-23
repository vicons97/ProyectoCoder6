
from sqlite3 import Cursor
from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from App_zap.forms import AccesorioFormulario, SucursalFormulario

from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView

from App_zap.models import Accesorios, Proveedores, Sucursales, Zapatos

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




   # def accesorioFormulario(request):

   #     if request.method == 'POST':
   #         accesorios = Accesorios(modelo = request.POST['modelo'], color = request.POST['color'], talla = request.POST['talla'], precio=request.POST['precio'])

   #        accesorios.save()

   #         return render(request, 'inicio.html')


   #    return render(request, "accesorioFormulario.html")



# Inicio de funcionalidades de Sucursales


def listaSucursales(request):

    sucursales = Sucursales.objects.all()

    contexto = {"sucursales": sucursales}

    return render(request, "leerSucursales.html", contexto)



def crea_sucursal(request):

    if request.method == 'POST':
    
        miFormulario = SucursalFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            sucursales = Sucursales(num_Sucursal = data['num_Sucursal'], nombre_sucursal = data['nombre_sucursal'], direccion = data['direccion'])
            sucursales.save()

            return render(request, 'inicio.html')

    else:

        miFormulario = SucursalFormulario()  

    return render(request, "sucursalesFormulario.html", {"miFormulario": miFormulario})


def eliminarSucursal(request, id):

    if request.method == 'POST':

        sucursal = Sucursales.objects.get(id = id)

        sucursal.delete()

        sucursales = Sucursales.objects.all()

        contexto = {"sucursales": sucursales}

        return render(request, "leerSucursales.html", contexto)  


def editar_sucursal(request, id):

    sucursal = Sucursales.objects.get(id = id)
    
    if request.method == 'POST':
    
        miFormulario = SucursalFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            sucursal.num_Sucursal = data["num_Sucursal"]
            sucursal.nombre_sucursal = data["nombre_sucursal"]
            sucursal.direccion = data["direccion"]
            sucursal.save()

            return render(request, 'inicio.html')

    else:

        miFormulario = SucursalFormulario(initial={

            "num_Sucursal": sucursal.num_Sucursal,
            "nombre_sucursal": sucursal.nombre_sucursal,
            "direccion": sucursal.direccion,
        })  

    return render(request, "editarFormulario.html", {"miFormulario": miFormulario, "id": sucursal.id})



#espacio para separar las funcionalidades de accesorios

def listaAccesorios(request):

    accesorios = Accesorios.objects.all()

    contexto = {"accesorios": accesorios}

    return render(request, "leerAccesorios.html", contexto)



def creaAccesorio(request):

    if request.method == 'POST':
    
        miFormulario = AccesorioFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            accesorios = Accesorios(modelo = data['modelo'], color = data['color'], talla = data['talla'], precio = data['precio'])
            accesorios.save()

            return render(request, 'inicio.html')

    else:

        miFormulario = AccesorioFormulario()  

    return render(request, "accesoriosFormulario.html", {"miFormulario": miFormulario})


def eliminarAccesorio(request, id):

    if request.method == 'POST':

        accesorios = Accesorios.objects.get(id = id)

        accesorios.delete()

        accesorios = Accesorios.objects.all()

        contexto = {"accesorios": accesorios}

        return render(request, "leerAccesorios.html", contexto)  


def editarAccesorio(request, id):

    accesorios = Accesorios.objects.get(id = id)
    
    if request.method == 'POST':
    
        miFormulario = AccesorioFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            accesorios.modelo = data["modelo"]
            accesorios.color = data["color"]
            accesorios.talla = data["talla"]
            accesorios.precio = data["precio"]
            accesorios.save()

            return render(request, 'inicio.html')

    else:

        miFormulario = AccesorioFormulario(initial={

            "modelo": accesorios.modelo,
            "color": accesorios.color,
            "talla": accesorios.talla,
            "precio": accesorios.precio,
        })  

    return render(request, "editarAccesorio.html", {"miFormulario": miFormulario, "id": accesorios.id})










class ProveedorList(ListView):

    model = Proveedores
    template_name = 'proveedor_list.html'
    context_object_name = 'proveedores'

class ProveedorDetail(DetailView):

    model = Proveedores
    template_name = 'proveedor-detail.html'
    context_object_name = 'proveedor'

class ProveedorCreate(CreateView):

    model = Proveedores
    template_name = 'proveedor_create.html'
    fields = ["nombre", "email", "fecha_de_afiliacion"]
    success_url = '/App_zap/'

class ProveedorUpdate(UpdateView):

    model = Proveedores 
    success_url = '/App_zap/'
    fields = ["nombre", "email", "fecha_de_afiliacion"]
    
   

class ProveedorDelete(DeleteView):

    model = Proveedores
    success_url = '/App_zap/'



