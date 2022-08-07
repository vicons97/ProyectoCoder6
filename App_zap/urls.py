
from django.urls import path

from App_zap.views import ProveedorCreate, ProveedorDelete, ProveedorDetail, ProveedorList, ProveedorUpdate, accesorioFormulario, accesorios, buscar, busquedaModelo, crea_sucursal, editar_sucursal, eliminarSucursal, lista_zapatos, listaSucursales, proveedores, sucursales, zapato, zapatos, inicio

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
    path('listaSucursales/',listaSucursales, name="listaSucursales"),
    path('crea-Sucursales/',crea_sucursal, name="creaSucursal"),
    path('elimina-sucursal/<int:id>',eliminarSucursal, name="eliminarSucursal"),
    path('edita-sucursal/<int:id>',editar_sucursal, name="editarSucursal"),
    path('listaProveedores/',ProveedorList.as_view(), name="listaProveedores"),
    path('detalleProveedores/',ProveedorDetail.as_view(), name="proveedor-detail"),
    path('creaProveedores/',ProveedorCreate.as_view(), name="creaProveedor"),
    path('UpdateProveedores/',ProveedorUpdate.as_view(), name="UpdateProveedor"),
    path('DeleteProveedores/',ProveedorDelete.as_view(), name="DeleteProveedor"),


]

