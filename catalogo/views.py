from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Producto
from .forms import ProductoForm


# FBV — vista de inicio
def home(request):
    categorias = Producto.CATEGORIAS
    total_productos = Producto.objects.filter(disponible=True).count()
    context = {
        'categorias': categorias,
        'total_productos': total_productos,
    }
    return render(request, 'catalogo/home.html', context)


# CBV — catálogo completo con ListView
class ProductoListView(ListView):
    model = Producto
    template_name = 'catalogo/catalogo.html'
    context_object_name = 'productos'

    def get_queryset(self):
        qs = Producto.objects.filter(disponible=True).order_by('-fecha_agregado')
        categoria = self.request.GET.get('categoria')
        if categoria:
            qs = qs.filter(categoria=categoria)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Producto.CATEGORIAS
        context['categoria_activa'] = self.request.GET.get('categoria', '')
        return context


# FBV — agregar producto desde la interfaz web
def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogo:catalogo')
    else:
        form = ProductoForm()
    return render(request, 'catalogo/agregar_producto.html', {'form': form})
