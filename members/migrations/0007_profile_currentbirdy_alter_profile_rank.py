# Generated by Django 4.1.5 on 2023-01-02 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_profile_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='currentBirdy',
            field=models.ImageField(default='static/images/birdy.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rank',
            field=models.IntegerField(default=5),
        ),
    ]
