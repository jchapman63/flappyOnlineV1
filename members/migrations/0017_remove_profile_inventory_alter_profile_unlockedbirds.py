# Generated by Django 4.1.5 on 2023-01-03 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0016_darkbluebirdy_name_defaultbirdy_name_greenbirdy_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='inventory',
        ),
        migrations.AlterField(
            model_name='profile',
            name='unlockedBirds',
            field=models.JSONField(default={'Default': True}),
        ),
    ]