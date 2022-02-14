# Generated by Django 3.2.11 on 2022-02-08 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_rename_estatus_proveedor_activo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articulo',
            old_name='ultimo_precio_compra_con_iva',
            new_name='precio_compra_con_iva',
        ),
        migrations.RenameField(
            model_name='articulo',
            old_name='ultimo_precio_compra_sin_iva',
            new_name='precio_compra_sin_iva',
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='activo',
            field=models.CharField(choices=[('S', 'S'), ('N', 'N')], default='S', max_length=1),
        ),
    ]