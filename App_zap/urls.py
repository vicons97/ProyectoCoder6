
from django.urls import path

from App_zap.views import ProveedorCreate, ProveedorDelete, ProveedorDetail, ProveedorList, ProveedorUpdate, accesorios, crea_sucursal, creaAccesorio, editar_sucursal, editarAccesorio, eliminarAccesorio, eliminarSucursal, listaAccesorios, listaSucursales, proveedores, sucursales, zapatos, inicio

urlpatterns = [
    
    path('zapatos/',zapatos, name="Zapatos"),
    path('accesorios/',accesorios, name="Accesorios"),
    path('proveedores/',proveedores, name="Proveedores"),
    path('sucursales/',sucursales, name="Sucursales"),
    
    path('',inicio, name="Inicio"),
    
    
    
    #Funcionalidad Sucursales
    path('listaSucursales/',listaSucursales, name="listaSucursales"),
    path('crea-Sucursales/',crea_sucursal, name="creaSucursal"),
    path('elimina-sucursal/<int:id>',eliminarSucursal, name="eliminarSucursal"),
    path('edita-sucursal/<int:id>',editar_sucursal, name="editarSucursal"),


    #Funcionalidad Accesorios
    path('listaAccesorios/',listaAccesorios, name="listaAccesorios"),
    path('creaAccesorios/',creaAccesorio, name="creaAccesorios"),
    path('eliminaAccesorios/<int:id>',eliminarAccesorio, name="eliminaAccesorios"),
    path('editaAccesorios/<int:id>',editarAccesorio, name="editaAccesorios"),


    path('listaProveedores/',ProveedorList.as_view(), name="listaProveedores"),
    path('detalleProveedores/<int:pk>',ProveedorDetail.as_view(), name="proveedor_detail"),
    path('creaProveedores/',ProveedorCreate.as_view(), name="creaProveedor"),
    path('UpdateProveedores/',ProveedorUpdate.as_view(), name="UpdateProveedor"),
    path('DeleteProveedores/',ProveedorDelete.as_view(), name="DeleteProveedor"),


]

