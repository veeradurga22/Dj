# Generated by Django 4.1 on 2022-08-13 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0018_alter_product_image_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
