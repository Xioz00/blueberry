# Generated by Django 4.2.1 on 2023-09-08 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_products_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]