# Generated by Django 4.2.3 on 2023-08-01 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donacion', '0007_rename_recaudos_principal_monto_recaudado_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='principal',
            old_name='monto_a_recuadar',
            new_name='monto_a_recaudar',
        ),
    ]
