from django.contrib import admin
from .models import Pitch, Sport, GameSession, Message

# Register your models here.

admin.site.register(Pitch)
admin.site.register(Sport)
admin.site.register(GameSession)
admin.site.register(Message)
