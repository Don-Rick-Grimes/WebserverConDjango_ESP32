from django.shortcuts import render
from .models import CategoriaProd, Producto
# Create your views here.


def tienda(request):
    productos = Producto.objects.all()
    categorias = CategoriaProd.objects.all()
    return render(request, "tienda/tienda.html", {"productos": productos, "categorias": categorias})


def categoriaProd(request, categoria_id):
    productos = Producto.objects.filter(categoria=categoria_id)
    categorias = CategoriaProd.objects.all()
    categoria = CategoriaProd.objects.get(id=categoria_id)
    return render(request, "tienda/categoriaProd.html", {"categoria": categoria, "productos": productos, "categorias": categorias})
