# Generated by Django 4.1.5 on 2023-01-03 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0017_remove_profile_inventory_alter_profile_unlockedbirds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='currentBirdy',
            field=models.ImageField(default='images/birdy.png', upload_to=''),
        ),
    ]
