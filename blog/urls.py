from django.urls import path
from .views import blog, categoria

urlpatterns = [
    path('', blog, name='blog'),
    path('categoria/<categoria_id>/', categoria, name='categoria'),
]