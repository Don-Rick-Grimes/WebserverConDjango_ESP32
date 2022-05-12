from django.urls import path
from .views import servicios

urlpatterns = [
    path('', servicios, name='servicios'),
]