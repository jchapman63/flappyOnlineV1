# Generated by Django 4.1.2 on 2023-01-10 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0020_alter_profile_currentbirdy_alter_profile_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='currentBirdyDown',
            field=models.CharField(default='images/birdyDown.png', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='currentBirdy',
            field=models.CharField(default='images/birdy.png', max_length=100),
        ),
    ]