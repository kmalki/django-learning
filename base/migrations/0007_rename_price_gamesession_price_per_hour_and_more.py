# Generated by Django 4.1.2 on 2022-10-11 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_game_time_gamesession_game_begin_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamesession',
            old_name='price',
            new_name='price_per_hour',
        ),
        migrations.RemoveField(
            model_name='gamesession',
            name='game_end',
        ),
        migrations.AddField(
            model_name='gamesession',
            name='hours',
            field=models.IntegerField(null=True),
        ),
    ]
