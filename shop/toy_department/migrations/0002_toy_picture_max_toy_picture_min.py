# Generated by Django 4.2.16 on 2024-10-14 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toy_department', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='toy',
            name='picture_max',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='toy',
            name='picture_min',
            field=models.CharField(default='', max_length=100),
        ),
    ]
