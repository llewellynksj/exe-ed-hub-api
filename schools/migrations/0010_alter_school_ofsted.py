# Generated by Django 3.2.23 on 2023-11-19 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0009_auto_20231119_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='ofsted',
            field=models.CharField(choices=[(1, '1 - Outstanding'), (2, '2 - Good'), (3, '3 - Requires Improvement'), (4, '4 - Inadequate')], max_length=255),
        ),
    ]