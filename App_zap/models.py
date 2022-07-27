from django.db import models


# Create your models here.

class Proveedores(models.Model):

    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    fecha_de_afiliacion = models.DateField(null=False, max_length=50)

    def __str__(self):
        return f'{self.nombre} - {self.fecha_de_afiliacion}'


class Zapatos(models.Model):

    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    talla = models.FloatField()
    precio = models.FloatField()
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE, default=1)

    def __str__(self) -> str:
        return f'{self.modelo} - {self.color} - {self.talla}'

    class Meta():
        verbose_name = 'My Shoe'
        verbose_name_plural = "My Shoes"
        ordering = ('-modelo','-talla')
        unique_together = ('modelo','talla')


class Accesorios(models.Model):

    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    talla = models.FloatField()
    precio = models.FloatField()
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.modelo} - {self.talla} - {self.color} - {self.proveedor}'


class Sucursales(models.Model):

    num_Sucursal = models.IntegerField()
    nombre_sucursal = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.num_Sucursal} - {self.nombre_sucursal}'

    