# Generated by Django 5.1.6 on 2025-03-05 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Res_name', models.CharField(max_length=100)),
                ('Food_cat', models.CharField(max_length=200)),
                ('rating', models.FloatField()),
                ('img', models.URLField(default='https://png.pngtree.com/png-vector/20200729/ourmid/pngtree-small-restaurant-building-vector-with-flat-design-png-image_2316583.jpg')),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
