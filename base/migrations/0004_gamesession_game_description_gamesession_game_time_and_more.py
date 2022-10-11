# Generated by Django 4.1.2 on 2022-10-11 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_pitch_name_alter_pitch_sport'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamesession',
            name='game_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='gamesession',
            name='game_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='gamesession',
            name='nb_places',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='gamesession',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]