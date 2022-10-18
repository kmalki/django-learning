from rest_framework.decorators import api_view
from rest_framework.response import Response
import rest_framework.status as status
from .serializers import GameSessionSerializer

from base.models import GameSession


@api_view(['GET'])
def get_routes(request):
    routes = ['GET api/', 'GET api/game_sessions', 'GET api/game_sessions/:id']
    return Response(data={'routes': routes}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_game_sessions(request):
    games = GameSession.objects.all()
    serializer = GameSessionSerializer(games, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_game_session(request, id):
    game = GameSession.objects.get(id=id)
    serializer = GameSessionSerializer(game)
    return Response(serializer.data, status=status.HTTP_200_OK)
