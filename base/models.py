from django.db import models
from django.contrib.auth.models import User


# Create your models here.

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
    leader = models.ForeignKey(User, on_delete=models.CASCADE)
    pitch = models.ForeignKey(Pitch, on_delete=models.CASCADE)
    game_begin = models.DateTimeField(null=True)
    hours = models.IntegerField(null=True)
    price_per_hour = models.FloatField(null=True)
    game_description = models.TextField(null=True)
    nb_places = models.IntegerField(null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['game_begin', '-updated']

    def __str__(self):
        return f"id: {str(self.id)} - pitch: { {str(self.pitch)} }"


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(GameSession, on_delete=models.CASCADE)
    body = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"id: {str(self.id)} - game_session: { {str(self.session)} } - body: {str(self.body)[0:50]}"
