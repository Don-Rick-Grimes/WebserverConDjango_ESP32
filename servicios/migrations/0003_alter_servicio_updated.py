# Generated by Django 4.0 on 2022-01-25 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_alter_servicio_contenido_alter_servicio_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
