# Generated by Django 4.1.2 on 2022-10-11 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_gamesession_game_description_gamesession_game_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='body',
            field=models.TextField(null=True),
        ),
    ]
