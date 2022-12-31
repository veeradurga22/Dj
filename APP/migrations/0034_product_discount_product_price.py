# Generated by Django 4.1 on 2022-12-21 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0033_rename_price_product_mrp'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]