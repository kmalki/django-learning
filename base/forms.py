from django.forms import ModelForm, DateTimeInput
from .models import GameSession


class GameSessionForm(ModelForm):
    class Meta:
        model = GameSession
        fields = ['leader', 'pitch', 'game_begin', 'hours', 'price_per_hour', 'game_description', 'nb_places']
        widgets = {
            'game_begin': DateTimeInput()
        }
