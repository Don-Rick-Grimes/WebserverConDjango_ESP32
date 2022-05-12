from django.urls import path
from .views import esp32

urlpatterns = [
    path('', esp32, name='esp32'),
]