
from django.urls import path

from App_zap.views import accesorioFormulario, accesorios, buscar, busquedaModelo, lista_zapatos, proveedores, sucursales, zapato, zapatos, inicio

urlpatterns = [
    
    path('zapatos/',zapatos, name="Zapatos"),
    path('accesorios/',accesorios, name="Accesorios"),
    path('proveedores/',proveedores, name="Proveedores"),
    path('sucursales/',sucursales, name="Sucursales"),
    path('',inicio, name="Inicio"),
    path('agrega-zapato/<modelo>/<talla>/<color>/<precio>/', zapato),
    path('lista-zapatos/',lista_zapatos),
    path('accesorioFormulario/',accesorioFormulario, name="accesorioFormulario"),
    path('busquedaModelo/',busquedaModelo, name="busquedaModelo"),
    path('buscar/',buscar, name="buscar"),
]

