from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('playersind', views.playersind, name='playersind'),
    path('playerplusesind', views.playerplusesind, name='playerplusesind'),
    path('playerstatind', views.playerstatind, name='playerstatind'),
]
