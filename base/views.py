from django.http import HttpRequest, HttpResponse


# Create your views here.


def home(HttpRequest):
    return HttpResponse('Home here')


def iss(HttpRequest):
    return HttpResponse('iss')
