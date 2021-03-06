# Generated by Django 2.2.2 on 2019-07-21 21:15

import MundoFastWebApp.models
from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('MundoFastWebApp', '0004_auto_20190720_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagenProducto',
            field=django_resized.forms.ResizedImageField(crop=None, default='Imagen-no-disponible.png', force_format=None, keep_meta=True, quality=0, size=[500, 300], storage=MundoFastWebApp.models.OverwriteStorage(), upload_to=MundoFastWebApp.models.content_file_name),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='imagenUsuario',
            field=django_resized.forms.ResizedImageField(crop=None, default='Imagen-no-disponible.png', force_format=None, keep_meta=True, quality=0, size=[500, 300], storage=MundoFastWebApp.models.OverwriteStorage(), upload_to=MundoFastWebApp.models.content_file_name),
        ),
    ]
