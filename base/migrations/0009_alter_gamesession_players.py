# Generated by Django 4.1.2 on 2022-10-12 19:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0008_alter_gamesession_options_alter_pitch_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesession',
            name='players',
            field=models.ManyToManyField(null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]