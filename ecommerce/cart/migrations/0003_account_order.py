# Generated by Django 5.0.3 on 2024-03-27 08:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_rename_quatity_cart_quantity'),
        ('shop', '0002_product'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acctnum', models.BigIntegerField()),
                ('accttype', models.CharField(max_length=25)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_items', models.IntegerField()),
                ('phone', models.BigIntegerField()),
                ('address', models.TextField()),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('order_status', models.CharField(default='Pending', max_length=35)),
                ('delivery_status', models.CharField(default='Pending', max_length=35)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
