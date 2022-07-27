from django.db import models

# Create your models here.

class Zapatos(models.Model):

    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    talla = models.FloatField()
    precio = models.FloatField()

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

class Proveedores(models.Model):

    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    fecha_de_afiliacion = models.DateField(null=False, max_length=50)

class Sucursales(models.Model):

    num_Sucursal = models.IntegerField()
    nombre_sucursal = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

    