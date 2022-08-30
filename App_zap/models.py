from django.db import models


# Create your models here.

class Proveedores(models.Model):

    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    fecha_de_afiliacion = models.DateField(null=False, max_length=50)

    def __str__(self):
        return f'NOMBRE:{self.nombre} - EMAIL:{self.email}'


class Zapatos(models.Model):

    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    talla = models.FloatField()
    precio = models.FloatField()

    def __str__(self) -> str:
        return f'MODELO:{self.modelo} - COLOR:{self.color} - TALLA:{self.talla}'

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

    def __str__(self):
        return f':MODELO:{self.modelo} - COLOR:{self.color} - TALLA:{self.talla}'


class Sucursales(models.Model):

    num_Sucursal = models.IntegerField()
    nombre_sucursal = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return f'NUM. SUCURSAL:{self.num_Sucursal} - NOMBRE:{self.nombre_sucursal}'


class Opiniones(models.Model):

    titulo = models.CharField(max_length=50)
    comentario = models.CharField(max_length=500)
    usuario = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f'TITULO: {self.titulo}:  COMENTARIOS:{self.comentario}. - USUARIO:{self.usuario} - EMAIL:{self.usuario}'