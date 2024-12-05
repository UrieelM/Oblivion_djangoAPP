# Generated by Django 5.1.3 on 2024-12-04 21:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('usuario_id', models.IntegerField()),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado_pedido', models.CharField(choices=[('pendiente', 'Pendiente'), ('procesado', 'Procesado'), ('enviado', 'Enviado'), ('completado', 'Completado'), ('cancelado', 'Cancelado')], default='pendiente', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('sku', models.CharField(max_length=100, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('talla', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(blank=True, max_length=50, null=True)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='uploads/producto/')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='store.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id_inventario', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.PositiveIntegerField(default=0)),
                ('producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='inventario', to='store.producto')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id_detalle_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.PositiveIntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sku', models.CharField(max_length=100)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='store.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detalles', to='store.producto')),
            ],
        ),
    ]
