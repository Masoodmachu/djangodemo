# Generated by Django 5.0.3 on 2024-03-29 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_account_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='acctnum',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='account',
            name='amount',
            field=models.BigIntegerField(),
        ),
    ]
