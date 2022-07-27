from django.contrib import admin

from App_zap.models import Accesorios, Proveedores, Sucursales, Zapatos

# Register your models here.

class ZapatoAdmin(admin.ModelAdmin):
    list_display = ['modelo', 'talla', "color", "precio"]
    search_fields = ['modelo', "talla", "color", "precio"]

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ["nombre", "email", "fecha_de_afiliacion"]
    search_fields = ["nombre", "email", "fecha_de_afiliacion"]


class AccesorioAdmin(admin.ModelAdmin):
    list_display = ['modelo', 'talla', "color", "precio"]
    search_fields = ['modelo', "talla", "color", "precio"]

class SucursalAdmin(admin.ModelAdmin):
    list_display = ["num_Sucursal", "nombre_sucursal"]
    search_fields = ["num_Sucursal", "nombre_sucursal", "direccion"]



admin.site.register(Zapatos, ZapatoAdmin)
admin.site.register(Proveedores, ProveedorAdmin)
admin.site.register(Accesorios, AccesorioAdmin)
admin.site.register(Sucursales, SucursalAdmin)

