# Generated by Django 4.1.6 on 2023-02-15 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('coordinates', models.IntegerField()),
                ('information', models.CharField(max_length=200)),
                ('report', models.CharField(max_length=201)),
            ],
        ),
    ]
