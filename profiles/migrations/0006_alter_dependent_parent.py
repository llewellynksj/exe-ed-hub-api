# Generated by Django 3.2.23 on 2023-11-20 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_dependent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dependent',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dependents', to='profiles.parentprofile'),
        ),
    ]
