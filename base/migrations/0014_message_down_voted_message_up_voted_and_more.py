# Generated by Django 4.1.2 on 2022-10-14 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0013_message_down_message_up'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='down_voted',
            field=models.ManyToManyField(blank=True, related_name='down_voters', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='up_voted',
            field=models.ManyToManyField(blank=True, related_name='up_voters', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
