from django.db import models


class Producto(models.Model):
    CATEGORIAS = [
        ('laptops', 'Laptops'),
        ('celulares', 'Celulares'),
        ('accesorios', 'Accesorios'),
        ('audio', 'Audio'),
    ]

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    stock = models.IntegerField(default=0)
    disponible = models.BooleanField(default=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_agregado']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return f'{self.nombre} — S/ {self.precio}'
