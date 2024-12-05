# Generated by Django 5.1.3 on 2024-12-05 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_detallepedido_precio_remove_detallepedido_sku_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagen',
            name='producto',
        ),
        migrations.AddField(
            model_name='imagen',
            name='descripcion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagenes_producto',
            field=models.ManyToManyField(blank=True, related_name='productos', to='store.imagen'),
        ),
    ]
