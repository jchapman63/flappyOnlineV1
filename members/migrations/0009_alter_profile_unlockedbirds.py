# Generated by Django 4.1.5 on 2023-01-02 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_profile_unlockedbirds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='unlockedBirds',
            field=models.JSONField(default={'Dark Blue': False, 'Default': True, 'Green': False, 'Lite Blue': False, 'Pink': False, 'Red': False}),
        ),
    ]
