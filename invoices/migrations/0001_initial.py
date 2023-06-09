# Generated by Django 3.2.19 on 2023-05-16 03:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('phone', models.IntegerField(default='09033873459')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('purchase_date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('phone', models.IntegerField(default='09033873459')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('date', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
