# Generated by Django 3.2.23 on 2023-11-19 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0006_school_overall_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='teaching_quality',
            field=models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
