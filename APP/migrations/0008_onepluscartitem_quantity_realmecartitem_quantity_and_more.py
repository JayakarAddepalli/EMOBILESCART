# Generated by Django 5.0.1 on 2024-03-16 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0007_cartitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='onepluscartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='realmecartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='redmicartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='samsungcartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
