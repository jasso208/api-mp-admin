# Generated by Django 3.2.11 on 2022-02-08 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_auto_20220208_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='nombre',
            field=models.CharField(default='', max_length=100),
        ),
    ]