from django.urls import path
from proyecto_web1App.views import home

urlpatterns = [
    path('', home, name='home'),
]