# Generated by Django 4.1.2 on 2022-10-14 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_gamesession_players'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='session',
        ),
        migrations.AddField(
            model_name='gamesession',
            name='messages',
            field=models.ManyToManyField(blank=True, to='base.message'),
        ),
    ]