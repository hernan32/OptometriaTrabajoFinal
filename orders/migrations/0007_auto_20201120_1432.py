# Generated by Django 3.1.3 on 2020-11-20 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20201114_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='frame',
            field=models.BooleanField(blank=True, null=True, verbose_name='Armazon'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_glass',
            field=models.BooleanField(default=True, verbose_name='Lente'),
        ),
        migrations.AddField(
            model_name='product',
            name='position',
            field=models.CharField(blank=True, choices=[('IZQ', 'Izquierda'), ('DER', 'Derecha')], max_length=3, null=True),
        ),
    ]
