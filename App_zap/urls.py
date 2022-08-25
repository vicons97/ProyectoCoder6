
from django.urls import path

from App_zap.views import accesorios, crea_sucursal, creaAccesorio, creaProveedor, creaZapato, editar_sucursal, editarAccesorio, editarProveedor, editarZapato, eliminarAccesorio, eliminarProveedor, eliminarSucursal, eliminarZapato, listaAccesorios, listaProveedores, listaSucursales, listaZapatos, loginView, proveedores, register, sucursales, zapatos, inicio

from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('zapatos/',zapatos, name="Zapatos"),
    path('accesorios/',accesorios, name="Accesorios"),
    path('proveedores/',proveedores, name="Proveedores"),
    path('sucursales/',sucursales, name="Sucursales"),
    
    path('',inicio, name="Inicio"),
    
    #Sucursales
    path('listaSucursales/',listaSucursales, name="listaSucursales"),
    path('crea-Sucursales/',crea_sucursal, name="creaSucursal"),
    path('elimina-sucursal/<int:id>',eliminarSucursal, name="eliminarSucursal"),
    path('edita-sucursal/<int:id>',editar_sucursal, name="editarSucursal"),


    #Accesorios
    path('listaAccesorios/',listaAccesorios, name="listaAccesorios"),
    path('creaAccesorios/',creaAccesorio, name="creaAccesorios"),
    path('eliminaAccesorios/<int:id>',eliminarAccesorio, name="eliminaAccesorios"),
    path('editaAccesorios/<int:id>',editarAccesorio, name="editaAccesorios"),

    #Zapatos
    path('listaZapatos/',listaZapatos, name="listaZapatos"),
    path('creaZapatos/',creaZapato, name="creaZapatos"),
    path('eliminaZapatos/<int:id>',eliminarZapato, name="eliminaZapatos"),
    path('editaZapatos/<int:id>',editarZapato, name="editaZapatos"),


    #Proveedores
    path('listaProveedores/',listaProveedores, name="listaProveedores"),
    path('creaProveedores/',creaProveedor, name="creaProveedores"),
    path('eliminaProveedores/<int:id>',eliminarProveedor, name="eliminaProveedores"),
    path('editaProveedores/<int:id>',editarProveedor, name="editaProveedores"),


    #Login
    path('login/', loginView, name='Login'),
    path('registrar/', register, name='Registrar'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='Logout'),

]



