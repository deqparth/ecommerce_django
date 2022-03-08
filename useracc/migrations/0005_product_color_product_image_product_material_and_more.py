# Generated by Django 4.0.2 on 2022-03-07 10:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useracc', '0004_cart_wishlist_cartitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=None, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='material',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]