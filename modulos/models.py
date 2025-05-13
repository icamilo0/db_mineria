from django.db import models

# Create your models here.

class Articulo(models.Model):
    descripcion = models.TextField("Descripción", null=True, blank=True)
    precio = models.DecimalField("Precio", max_digits=15, decimal_places=2, null=True, blank=True)
    modelo = models.PositiveIntegerField("Modelo", null=True, blank=True)
    kilometraje = models.DecimalField("Kilometraje", max_digits=15, decimal_places=2, null=True, blank=True)
    lugar_de_venta = models.TextField("Lugar de Venta", null=True, blank=True)

    class Meta:
        db_table = 'articulos'
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'

    def __str__(self):
        return f'{ self.descripcion } - { self.precio }'