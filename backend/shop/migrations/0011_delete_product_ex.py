# Generated by Django 5.1.2 on 2024-10-14 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_rename_pruduct_product_ex_remove_product_pruduct'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product_ex',
        ),
    ]
