# Generated by Django 4.0.6 on 2022-08-29 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_zap', '0003_zapatos_proveedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opiniones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('comentario', models.CharField(max_length=500)),
                ('usuario', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]