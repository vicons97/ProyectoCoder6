
from django.urls import path

from App_zap.views import accesorios, proveedores, sucursales, zapatos, inicio

urlpatterns = [
    
    path('zapatos/',zapatos),
    path('accesorios/',accesorios),
    path('proveedores/',proveedores),
    path('sucursales/',sucursales),
    path('',inicio),
]