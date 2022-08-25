
from sqlite3 import Cursor
from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from App_zap.forms import AccesorioFormulario, ProveedorFormulario, SucursalFormulario, ZapatoFormulario
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate

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

def about(self):
    
    return render(self, "about.html")



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


#Inicio de funcionalidades para Zapatos

def listaZapatos(request):

    zapatos = Zapatos.objects.all()

    contexto = {"zapatos": zapatos}

    return render(request, "leerZapatos.html", contexto)



def creaZapato(request):

    if request.method == 'POST':
    
        miFormulario = ZapatoFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            zapatos = Zapatos(modelo = data['modelo'], color = data['color'], talla = data['talla'], precio = data['precio'])
            zapatos.save()

            return render(request, 'inicio.html')

    else:

        miFormulario = ZapatoFormulario()  

    return render(request, "zapatosFormulario.html", {"miFormulario": miFormulario})


def eliminarZapato(request, id):

    if request.method == 'POST':

        zapatos = Zapatos.objects.get(id = id)

        zapatos.delete()

        zapatos = Zapatos.objects.all()

        contexto = {"zapatos": zapatos}

        return render(request, "leerZapatos.html", contexto)  


def editarZapato(request, id):

    zapatos = Zapatos.objects.get(id = id)
    
    if request.method == 'POST':
    
        miFormulario = ZapatoFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            zapatos.modelo = data["modelo"]
            zapatos.color = data["color"]
            zapatos.talla = data["talla"]
            zapatos.precio = data["precio"]
            zapatos.save()

            return render(request, 'inicio.html')

    else:

        miFormulario = ZapatoFormulario(initial={

            "modelo": zapatos.modelo,
            "color": zapatos.color,
            "talla": zapatos.talla,
            "precio": zapatos.precio,
        })  

    return render(request, "editarZapato.html", {"miFormulario": miFormulario, "id": zapatos.id})


#Inicio de funcionalidades para Proveedores

def listaProveedores(request):

    proveedores = Proveedores.objects.all()

    contexto = {"proveedores": proveedores}

    return render(request, "leerProveedores.html", contexto)



def creaProveedor(request):

    if request.method == 'POST':
    
        miFormulario = ProveedorFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            proveedores = Proveedores(nombre = data['nombre'], email = data['email'], fecha_de_afiliacion = data['fecha_de_afiliacion'])
            proveedores.save()

            return render(request, 'inicio.html')

    else:

        miFormulario = ProveedorFormulario()  

    return render(request, "proveedoresFormulario.html", {"miFormulario": miFormulario})


def eliminarProveedor(request, id):

    if request.method == 'POST':

        proveedores = Proveedores.objects.get(id = id)

        proveedores.delete()

        proveedores = Proveedores.objects.all()

        contexto = {"proveedores": proveedores}

        return render(request, "leerProveedores.html", contexto)  


def editarProveedor(request, id):

    proveedores = Proveedores.objects.get(id = id)
    
    if request.method == 'POST':
    
        miFormulario = ProveedorFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            proveedores.nombre = data["nombre"]
            proveedores.email = data["email"]
            proveedores.fecha_de_afiliacion = data["fecha_de_afiliacion"]
            proveedores.save()

            return render(request, 'inicio.html')

    else:

        miFormulario = ProveedorFormulario(initial={

            "nombre": proveedores.nombre,
            "email": proveedores.email,
            "fecha_de_afiliacion": proveedores.fecha_de_afiliacion,
        })  

    return render(request, "editarProveedores.html", {"miFormulario": miFormulario, "id": proveedores.id})


    #FUNCION DE LOGIN
def loginView(request):
    
    if request.method == 'POST':

        miFormulario = AuthenticationForm(request, data=request.POST)

        if miFormulario.is_valid():   

            data = miFormulario.cleaned_data

            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)
            
            if  user: 

                login(request, user)
                
                return render(request, "inicioLogin.html", {"mensaje": f'Bienvenido {usuario}'})
            
            else:

                return render(request, "inicioLogin.html", {"mensaje": f'Error, datos incorrectos'})
    
        return render(request, "inicioLogin.html", {"mensaje": f'Lo Datos de acceso son invalidos, vuelva a iniciar sesion, recuerde colocar bien su password'})
    
    else:
        miFormulario = AuthenticationForm()

        return render(request, "login.html", {"miFormulario": miFormulario})       


#FUNCION DE REGISTRAR
def register(request):  

    if request.method == 'POST':

        form = UserCreationForm (request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]

            form.save()

            return render(request, "inicioRegister.html" , {"mensanje": f'Usuario : {username} creado'})
    else:

        form = UserCreationForm ()

    return render(request, "registro.html", {"miFormulario": form})



