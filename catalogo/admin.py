from django.contrib import admin
from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'disponible', 'fecha_agregado')
    list_filter = ('categoria', 'disponible')
    search_fields = ('nombre', 'descripcion')
