# Generated by Django 5.0.1 on 2024-03-16 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0006_realmecartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
