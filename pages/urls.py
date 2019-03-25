from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('playersind', views.playersind, name='playersind'),
    path('playerplusind', views.playerplusind, name='playerplusind'),
    path('playerstatind', views.playerstatind, name='playerstatind'),
    path('standingsind', views.standingsind, name='standingsind'),
]
