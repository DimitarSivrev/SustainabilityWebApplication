# Generated by Django 4.1.5 on 2023-03-20 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_location_latitude_alter_location_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]