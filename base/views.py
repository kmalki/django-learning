from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .models import Pitch, GameSession, User, Sport, Message
from .forms import GameSessionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
    return render(request, 'base/login.html', {"page": "register", "form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Password incorrect")
        except ObjectDoesNotExist:
            messages.error(request, "User does not exist")
    return render(request, 'base/login.html', {"page": "login"})


@login_required()
def logout_view(request):
    logout(request)
    return redirect('home')


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
    game = GameSession.objects.get(id=int(game_id))
    return render(request, 'base/game_session.html', {'game': game})


@login_required(login_url="/login")
def create_game_session(request):
    form = GameSessionForm
    if request.method == 'POST':
        form = GameSessionForm(request.POST)
        if form.is_valid():
            game = form.save(commit=False)
            game.leader = request.user
            game.nb_places = game.nb_places - 1
            game.save()
            game.players.add(request.user)
            return redirect('game_session', game.id)
        else:
            return render(request, 'base/game_session_form.html', {'form': form, 'error': True, 'type': 'create'})
    return render(request, 'base/game_session_form.html', {'form': form, 'type': 'create'})


@login_required(login_url="/login")
def update_game_session(request, game_id):
    game = GameSession.objects.get(id=game_id)
    if game.leader != request.user:
        messages.error(request, 'You can update only your games')
        return redirect('home')
    form = GameSessionForm(instance=game)
    if request.method == 'POST':
        form = GameSessionForm(request.POST, instance=game)
        if form.is_valid():
            game = form.save()
            return redirect('game_session', game.id)
        else:
            return render(request, 'base/game_session_form.html', {'form': form, 'error': True, 'type': 'edit'})
    return render(request, 'base/game_session_form.html', {'form': form, 'type': 'edit'})


@login_required(login_url="/login")
def delete_game_session(request, game_id):
    game = GameSession.objects.get(id=game_id)
    if game.leader != request.user:
        messages.error(request, 'You can delete only your games')
        return redirect('home')
    if request.method == "POST":
        game.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'object': game})


def search_games(request):
    if request.GET.get("search") is None or request.GET.get("search") == "":
        return redirect('home')
    else:
        if request.GET.get("type") == "user":
            search_attribute = request.GET.get("search")
            games = GameSession.objects.filter(leader__username__iexact=search_attribute)
            sports = list(set([game.pitch.sport for game in games]))
        else:

            search_attribute = request.GET.get("search")
            games = GameSession.objects.filter(pitch__name__iexact=search_attribute)
            sports = list(set([game.pitch.sport for game in games]))
        if games.count() == 0:
            messages.error(request, "Search found 0 game")
            return redirect('home')
        return render(request, 'base/home.html', {'games': games, 'sports': sports})


@login_required(login_url='login')
def book_unbook_game_session(request):
    game_id = request.POST.get("game_id")
    user = request.user
    game = GameSession.objects.get(id=game_id)
    if request.POST.get("book") is not None:
        game.players.add(user)
        game.nb_places = game.nb_places - 1
        game.save()
        return redirect('home')
    elif request.POST.get("unbook") is not None:
        game.players.remove(user)
        game.nb_places = game.nb_places + 1
        game.save()
        return redirect('home')
    return redirect('home')


@login_required(login_url='login')
def remove_player(request):
    game = GameSession.objects.get(id=request.POST.get("game_id"))
    if request.user == game.leader:
        user = User.objects.get(id=request.POST.get("player_id"))
        game.players.remove(user)
        game.nb_places = game.nb_places + 1
        game.save()
        return redirect('game_session', game.id)
    return redirect('home')


@login_required(login_url='login')
def remove_message(request):
    game = GameSession.objects.get(id=request.POST.get("game_id"))
    message = Message.objects.get(id=request.POST.get("message_id"))
    if request.user == message.user:
        game.messages.remove(message)
        message.delete()
        game.save()
        return redirect('game_session', game.id)
    return redirect('home')


@login_required(login_url='login')
def up_down_message(request):
    game = GameSession.objects.get(id=request.POST.get("game_id"))
    message = Message.objects.get(id=request.POST.get("message_id"))
    if "up" in request.POST:
        if request.user in message.up_voted.all():
            message.up = message.up - 1
            message.up_voted.remove(request.user)
        else:
            message.up = message.up + 1
            message.up_voted.add(request.user)
        message.save()
    elif "down" in request.POST:
        if request.user in message.down_voted.all():
            message.down = message.down - 1
            message.down_voted.remove(request.user)
        else:
            message.down = message.down + 1
            message.down_voted.add(request.user)
        message.save()
    return redirect('game_session', game.id)


@login_required(login_url='login')
def invite_to_game_session(request):
    game = GameSession.objects.get(id=request.POST.get("game_id"))
    try:
        user = User.objects.get(username__iexact=request.POST.get("user_id"))
        if user != request.user and user not in game.players.all():
            game.pending.add(user)
            game.save()
        else:
            messages.error(request, "User already in game")
    except ObjectDoesNotExist:
        messages.error(request, "User does not exist")
    return redirect('game_session', game.id)


@login_required(login_url="login")
def join_from_invitation(request):
    game = GameSession.objects.get(id=request.POST.get("game_id"))
    try:
        user = request.user
        if user not in game.players.all() and user in game.pending.all() and game.nb_places > 0:
            game.pending.remove(user)
            game.players.add(user)
            game.nb_places = game.nb_places - 1
            game.save()
        else:
            messages.error(request, "User already in game")
    except ObjectDoesNotExist:
        messages.error(request, "User does not exist")
    return redirect('game_session', game.id)


@login_required(login_url="login")
def get_message_edition(request, game_id, message_id):
    message = Message.objects.get(id=message_id)
    if message.user == request.user:
        return render(request, 'base/edit_message.html', {"message": message, "game_id": game_id})


@login_required(login_url="login")
def edit_message(request):
    message = Message.objects.get(id=request.POST.get("message_id"))
    if message.user != request.user:
        return redirect("home")
    text_value = request.POST.get("message_value")
    message.body = text_value
    message.edited = True
    message.save()
    return redirect('game_session', request.POST.get("game_id"))


@login_required(login_url="login")
def add_message(request):
    text_value = request.POST.get("message_value")
    message = Message.objects.create(
        user=request.user,
        body=text_value
    )
    game = GameSession.objects.get(id=request.POST.get("game_id"))
    game.messages.add(message)
    game.save()
    return redirect('game_session', request.POST.get("game_id"))
