from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes),
    path('game_sessions', views.get_game_sessions),
    path('game_sessions/<str:id>', views.get_game_session)
]
