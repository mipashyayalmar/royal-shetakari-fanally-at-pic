# Generated by Django 5.2.1 on 2025-06-27 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_table_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='section',
            field=models.CharField(choices=[('HALL', 'Hall'), ('GARDEN', 'Garden'), ('TREE', 'Tree'), ('ZOPADI', 'Zopadi')], default='HALL', max_length=20),
        ),
    ]
