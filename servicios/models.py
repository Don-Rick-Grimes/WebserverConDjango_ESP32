from distutils.command.upload import upload
from django.db import models
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import create_many_to_many_intermediary_model

# Create your models here.

class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=80)
    imagen=models.ImageField(upload_to='servicios')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.titulo