from django.urls import path
from base import views

urlpatterns = [
    path('', views.home, name="home"),
    path('pitch/<str:pitch_id>', views.pitch, name="pitch")
]
