# Generated by Django 4.2.1 on 2023-09-08 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_products_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='available',
        ),
    ]