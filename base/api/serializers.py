from rest_framework.serializers import ModelSerializer
from base.models import GameSession


class GameSessionSerializer(ModelSerializer):
    class Meta:
        model = GameSession
        fields = '__all__'
