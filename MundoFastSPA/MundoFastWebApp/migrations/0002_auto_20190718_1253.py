# Generated by Django 2.2 on 2019-07-18 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MundoFastWebApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagenProducto',
            field=models.ImageField(default='Imagen-no-disponible.png', upload_to='productos'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoriaProducto',
            field=models.CharField(choices=[('Electro', 'Electrodomesticos'), ('Cocina', 'Articulos de Cocina'), ('Baño', 'Articulos de Baño'), ('Decoración', 'Articulos de Decoracion'), ('Jardín', 'Articulos de Jardineria'), ('Otros', 'Otros')], default='Electro', max_length=50),
        ),
    ]
