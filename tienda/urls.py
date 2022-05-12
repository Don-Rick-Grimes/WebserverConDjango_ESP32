from django.urls import path
from .views import tienda, categoriaProd

urlpatterns = [
    path('',tienda, name='tienda'),
    path('categoriaProd/<categoria_id>',categoriaProd, name='categoriaProd'),
]