from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='playerstat'),
	path('playerstat_search', views.playerstat_search, name='playerstat_search'),
	
]