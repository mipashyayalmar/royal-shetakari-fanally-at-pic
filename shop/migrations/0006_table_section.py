# Generated by Django 5.2.1 on 2025-06-27 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_product_product_id_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='section',
            field=models.CharField(choices=[('HALL', 'Hall'), ('GARDEN', 'Garden'), ('VIP', 'VIP Room'), ('TERRACE', 'Terrace')], default='HALL', max_length=20),
        ),
    ]
