from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    body = models.TextField(null=True)
    up = models.BigIntegerField(default=0)
    up_voted = models.ManyToManyField(User, blank=True, related_name="up_voters")
    down_voted = models.ManyToManyField(User, blank=True, related_name="down_voters")
    down = models.BigIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    edited = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f"id: {str(self.id)} - body: {str(self.body)[0:50]}"


class Sport(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{str(self.name)}"


class Pitch(models.Model):
    id = models.AutoField(primary_key=True)
    sport = models.ForeignKey(Sport, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{str(self.name)}"


class GameSession(models.Model):
    id = models.AutoField(primary_key=True)
    leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name="leader")
    pitch = models.ForeignKey(Pitch, on_delete=models.CASCADE)
    game_begin = models.DateTimeField(null=True)
    hours = models.IntegerField(null=True)
    price_per_hour = models.FloatField(null=True)
    game_description = models.TextField(null=True)
    nb_places = models.IntegerField(null=True)
    players = models.ManyToManyField(User, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    messages = models.ManyToManyField(Message, blank=True)
    pending = models.ManyToManyField(User, blank=True, related_name="pending")

    class Meta:
        ordering = ['game_begin', '-updated']

    def __str__(self):
        return str(self.id)
