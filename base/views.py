from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

pitchs = [{'id': 1, 'name': 'Terrain 1'}, {'id': 2, 'name': 'Terrain 2'}, {'id': 3, 'name': 'Terrain 3'},
          {'id': 4, 'name': 'Terrain 4'}]


def home(request):
    return render(request, 'base/home.html', {'pitchs': pitchs})


def pitch(request, pitch_id):
    p_res = None
    for p in pitchs:
        if p['id'] == int(pitch_id):
            p_res = p
    print(p_res)
    return render(request, 'base/pitch.html', {'pitch': p_res})
