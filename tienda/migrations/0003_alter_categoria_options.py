# Generated by Django 4.0 on 2022-01-28 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto_categorias'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'categoriaProd', 'verbose_name_plural': 'categoriasProd'},
        ),
    ]
