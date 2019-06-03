# Generated by Django 2.2 on 2019-06-03 00:02

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
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
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('rutUsuario', models.CharField(max_length=20)),
                ('nombreUsuario', models.CharField(max_length=50)),
                ('imagenUsuario', models.CharField(max_length=10000)),
                ('rolUsuario', models.CharField(max_length=20)),
                ('emailUsuario', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
