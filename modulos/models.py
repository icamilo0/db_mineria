from django.db import models

# Create your models here.


class Articulo(models.Model):
    descripcion = models.TextField("Descripción", null=True, blank=True)
    tienda = models.CharField("Tienda", max_length=255, null=True, blank=True)
    precio = models.DecimalField("Precio", max_digits=15, decimal_places=2, null=True, blank=True)
    modelo = models.PositiveIntegerField("Modelo", null=True, blank=True)
    kilometraje = models.DecimalField("Kilometraje", max_digits=15, decimal_places=2, null=True, blank=True)
    lugar_de_venta = models.TextField("Lugar de Venta", null=True, blank=True)
    url = models.TextField("URL", null=True, blank=True)
    marca = models.CharField("Color", max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'articulos'
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'

    def __str__(self):
        return f'{ self.descripcion } - { self.precio }'


class Rol(models.Model):
    rol = models.CharField("Rol", max_length=50, null=True, blank=True)
    descripcion = models.TextField("Descripción", null=True, blank=True)

    class Meta:
        db_table = 'roles'
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return f'{ self.rol } - { self.descripcion }'


class Usuario(models.Model):
    fk_rol = models.ForeignKey(Rol, verbose_name="Rol", on_delete=models.CASCADE)
    nombre = models.CharField("Nombre", max_length=50, null=True, blank=True)
    apellido = models.CharField("Apellido", max_length=50, null=True, blank=True)
    user = models.CharField("Usuario", max_length=150, unique=True)
    password = models.CharField("Contraseña", max_length=128)

    class Meta:
        db_table = 'usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'{ self.nombre } { self.apellido }'


# class NombreModelo(models.Model):
#     class Meta:
#         db_table = ''
#         verbose_name = ''
#         verbose_name_plural = ''

#     def __str__(self):
#         return f'{ self } - { self }'
