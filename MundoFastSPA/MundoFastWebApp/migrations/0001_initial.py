# Generated by Django 2.2.1 on 2019-05-29 03:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadProducto', models.PositiveIntegerField(default=1)),
                ('descuentoAplicadoProducto', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)])),
                ('totalPorProducto', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoProducto', models.IntegerField(unique=True)),
                ('nombreProducto', models.CharField(max_length=100)),
                ('descripcionProducto', models.CharField(max_length=500)),
                ('categoriaProducto', models.CharField(choices=[('Electro', 'Electrodomesticos'), ('Cocina', 'Articulos de Cocina'), ('Baño', 'Articulos de Baño'), ('Decoración', 'Articulos de Decoracion'), ('Jardín', 'Articulos de Jardineria')], default='Electro', max_length=50)),
                ('precioProducto', models.PositiveIntegerField(default=0)),
                ('cantidadProducto', models.PositiveIntegerField(default=0)),
                ('ofertaProducto', models.BooleanField(default=False)),
                ('descuentoProducto', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rutUsuario', models.CharField(max_length=20)),
                ('nombreUsuario', models.CharField(max_length=50)),
                ('emailUsuario', models.CharField(max_length=100)),
                ('imagenUsuario', models.CharField(max_length=10000)),
                ('rolUsuario', models.CharField(max_length=20)),
                ('passwordUsuario', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaVenta', models.DateTimeField(auto_now_add=True)),
                ('cuotasVenta', models.PositiveIntegerField(default=1)),
                ('totalVenta', models.PositiveIntegerField()),
                ('descuendoAdicionalVenta', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)])),
                ('productos', models.ManyToManyField(through='MundoFastWebApp.DetalleVenta', to='MundoFastWebApp.Producto')),
                ('responsableVenta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MundoFastWebApp.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MundoFastWebApp.Producto'),
        ),
        migrations.AddField(
            model_name='detalleventa',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MundoFastWebApp.Venta'),
        ),
    ]
