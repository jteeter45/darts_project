from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='playerplus'),
	path('playerplus_search', views.playerplus_search, name='playerplus_search'),
	
]