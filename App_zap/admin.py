from django.contrib import admin

from App_zap.models import Accesorios, Proveedores, Sucursales, Zapatos

# Register your models here.

class ZapatoAdmin(admin.ModelAdmin):
    list_display = ['modelo', 'talla', "color", "precio"]

admin.site.register(Zapatos, ZapatoAdmin)
admin.site.register(Proveedores)
admin.site.register(Accesorios)
admin.site.register(Sucursales)

