# Generated by Django 5.1.2 on 2024-10-14 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_pruduct_product_pruduct'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pruduct',
            new_name='Product_ex',
        ),
        migrations.RemoveField(
            model_name='product',
            name='pruduct',
        ),
    ]
