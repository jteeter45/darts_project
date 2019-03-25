from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='standings'),
    path('standings_search', views.standings_search, name='standings_search'),
]