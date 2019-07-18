# Generated by Django 2.2 on 2019-07-18 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MundoFastWebApp', '0002_auto_20190718_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='descripcionEmpresa',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='direccionEmpresa',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='emailEmpresa',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='horarioEmpresa',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='imagenEmpresa',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='nombreEmpresa',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='imagenUsuario',
            field=models.ImageField(default='Imagen-no-disponible.png', upload_to='usuarios'),
        ),
    ]
