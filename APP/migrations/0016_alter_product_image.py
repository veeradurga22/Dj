# Generated by Django 4.1 on 2022-08-13 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0015_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='./APP/Media/'),
        ),
    ]
