from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.apellido}'


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField(default=0) # Empieza en cero por df
    stock_actual = models.IntegerField(default=0)
    proveedor = models.ForeignKey(
        Proveedor,
        related_name='productos',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.nombre