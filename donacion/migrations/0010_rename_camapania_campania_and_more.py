# Generated by Django 4.2.3 on 2023-08-08 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donacion', '0009_camapania_categorias_donacion_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='camapania',
            new_name='campania',
        ),
        migrations.RemoveField(
            model_name='donacion',
            name='descripcion',
        ),
        migrations.AlterModelTable(
            name='campania',
            table='campañas',
        ),
    ]