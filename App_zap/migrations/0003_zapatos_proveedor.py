# Generated by Django 4.0.6 on 2022-07-27 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_zap', '0002_alter_zapatos_options_accesorios_proveedor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='zapatos',
            name='proveedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='App_zap.proveedores'),
        ),
    ]