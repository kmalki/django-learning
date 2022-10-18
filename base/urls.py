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
    path('searchGames', views.search_games, name="search_games"),
    path('register', views.register_view, name="register"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('book_unbook_session', views.book_unbook_game_session, name="book_unbook_game_session"),
    path('remove_player', views.remove_player, name="remove_player"),
    path('remove_message', views.remove_message, name="remove_message"),
    path('up_down_message', views.up_down_message, name="up_down_message"),
    path('invite_to_game_session', views.invite_to_game_session, name="invite_to_game_session"),
    path('join_from_invitation', views.join_from_invitation, name="join_from_invitation"),
    path('get_message_edition/<str:game_id>/<str:message_id>', views.get_message_edition, name="get_message_edition"),
    path('edit_message', views.edit_message, name="edit_message"),
    path('add_message', views.add_message, name="add_message")
]
