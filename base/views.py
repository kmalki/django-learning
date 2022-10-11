from django.shortcuts import render, redirect
from .models import Pitch, GameSession, User, Sport
from .forms import GameSessionForm


# Create your views here.


def home(request):
    if request.GET.get('sport') is not None:
        sport_param = request.GET.get('sport')
        sport = Sport.objects.filter(name=sport_param).first()
        games = GameSession.objects.filter(pitch__sport__id=sport.id)
        sports = [sport]
    else:
        games = GameSession.objects.all()
        sports = Sport.objects.all()
    return render(request, 'base/home.html', {'games': games, 'sports': sports})


def pitch(request, pitch_id):
    p_res = Pitch.objects.get(id=int(pitch_id))
    games = GameSession.objects.filter(pitch=p_res)
    return render(request, 'base/pitch.html', {'pitch': p_res, 'games_session': games})


def user(request, user_id):
    u_res = User.objects.get(id=int(user_id))
    return render(request, 'base/user.html', {'user': u_res})


def game_session(request, game_id):
    g_res = GameSession.objects.get(id=int(game_id))
    return render(request, 'base/game_session.html', {'game_session': g_res})


def create_game_session(request):
    form = GameSessionForm
    if request.method == 'POST':
        form = GameSessionForm(request.POST)
        if form.is_valid():
            print("no error")
            game = form.save()
            return redirect('game_session', game.id)
        else:
            return render(request, 'base/game_session_form.html', {'form': form, 'error': True, 'type': 'create'})
    return render(request, 'base/game_session_form.html', {'form': form, 'type': 'create'})


def update_game_session(request, game_id):
    game = GameSession.objects.get(id=game_id)
    form = GameSessionForm(instance=game)
    if request.method == 'POST':
        form = GameSessionForm(request.POST, instance=game)
        if form.is_valid():
            game = form.save()
            return redirect('game_session', game.id)
        else:
            return render(request, 'base/game_session_form.html', {'form': form, 'error': True, 'type': 'edit'})
    return render(request, 'base/game_session_form.html', {'form': form, 'type': 'edit'})


def delete_game_session(request, game_id):
    game = GameSession.objects.get(id=game_id)
    if request.method == "POST":
        game.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'object': game})
