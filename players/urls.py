from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='players'),
	path('players_search', views.players_search, name='players_search'),
	
]