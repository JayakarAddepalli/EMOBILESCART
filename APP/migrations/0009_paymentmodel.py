# Generated by Django 5.0.1 on 2024-03-18 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0008_onepluscartitem_quantity_realmecartitem_quantity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=254)),
                ('PhNo', models.IntegerField()),
                ('Address', models.TextField()),
                ('PinCode', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
