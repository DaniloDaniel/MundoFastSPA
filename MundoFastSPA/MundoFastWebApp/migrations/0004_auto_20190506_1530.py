# Generated by Django 2.2.1 on 2019-05-06 18:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MundoFastWebApp', '0003_auto_20190506_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descuentoProducto',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(100)]),
        ),
    ]
