# Generated by Django 4.1.2 on 2022-10-11 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_message_body'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamesession',
            old_name='game_time',
            new_name='game_begin',
        ),
        migrations.AddField(
            model_name='gamesession',
            name='game_end',
            field=models.DateTimeField(null=True),
        ),
    ]
