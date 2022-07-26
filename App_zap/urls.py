
from django.urls import path

from App_zap.views import accesorios, lista_zapatos, proveedores, sucursales, zapato, zapatos, inicio

urlpatterns = [
    
    path('zapatos/',zapatos),
    path('accesorios/',accesorios),
    path('proveedores/',proveedores),
    path('sucursales/',sucursales),
    path('',inicio),
    path('agrega-zapato/<modelo>/<talla>/<color>/<precio>/', zapato),
    path('lista-zapatos/',lista_zapatos),

]

