from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'stock', 'disponible']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ej: Laptop HP Pavilion 15'}),
            'descripcion': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Descripción del producto...'}),
            'precio': forms.NumberInput(attrs={'placeholder': '0.00', 'step': '0.01', 'min': '0'}),
            'stock': forms.NumberInput(attrs={'placeholder': '0', 'min': '0'}),
        }
        labels = {
            'nombre': 'Nombre del producto',
            'descripcion': 'Descripción',
            'precio': 'Precio (S/)',
            'categoria': 'Categoría',
            'stock': 'Stock disponible',
            'disponible': 'Mostrar en catálogo',
        }
