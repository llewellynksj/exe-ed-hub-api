# Generated by Django 3.2.23 on 2023-11-19 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0004_rename_city_school_locality_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='locality_name',
            field=models.CharField(choices=[('St Leonards', 'St Leonards'), ('Topsham', 'Topsham'), ('Pinhoe', 'Pinhoe'), ('Heavitress', 'Heavitree'), ('Matford', 'Matford'), ('Alphington', 'Alphington'), ('St Thomas', 'St Thomas'), ('Exminster', 'Exminster'), ('Central', 'Central'), ('Exmouth', 'Exmouth'), ('Whimple', 'Whimple'), ('Exwick', 'Exwick'), ('Newcourt', 'Newcourt'), ('Sowton', 'Sowton'), ('Countess Wear', 'Countess Wear')], max_length=255),
        ),
    ]