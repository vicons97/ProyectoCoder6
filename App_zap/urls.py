
from django.urls import path

from App_zap.views import accesorios, lista_zapatos, proveedores, sucursales, zapato, zapatos, inicio

urlpatterns = [
    
    path('zapatos/',zapatos, name="Zapatos"),
    path('accesorios/',accesorios, name="Accesorios"),
    path('proveedores/',proveedores, name="Proveedores"),
    path('sucursales/',sucursales, name="Sucursales"),
    path('',inicio, name="Inicio"),
    path('agrega-zapato/<modelo>/<talla>/<color>/<precio>/', zapato),
    path('lista-zapatos/',lista_zapatos),

]

