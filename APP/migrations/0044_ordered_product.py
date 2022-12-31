# Generated by Django 4.1 on 2022-12-30 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0043_order_item_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordered_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.order_item')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='APP.product')),
            ],
        ),
    ]