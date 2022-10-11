from django.urls import path
from base import views

urlpatterns = [
    path('', views.home, name="home"),
    path('pitch/<str:pitch_id>', views.pitch, name="pitch"),
    path('user/<str:user_id>', views.user, name="user"),
    path('gameSession/<str:game_id>', views.game_session, name="game_session"),
    path('createGameSession', views.create_game_session, name="create_game_session"),
    path('updateGameSession/<str:game_id>', views.update_game_session, name="update_game_session"),
    path('deleteGameSession/<str:game_id>', views.delete_game_session, name="delete_game_session"),

]
