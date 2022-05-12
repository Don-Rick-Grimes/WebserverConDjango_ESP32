from django.shortcuts import render
from .models import Categoria, Post
# Create your views here.
def blog(request):
    categorias = Categoria.objects.all()
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"categorias":categorias,"posts":posts})

def categoria(request, categoria_id):
    categorias = Categoria.objects.all()
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias = categoria_id)
    return render(request, "blog/categoria.html", {"categorias":categorias,"posts":posts,"categoria":categoria})    