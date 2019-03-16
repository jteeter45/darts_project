from django.shortcuts import render
from django.http import HttpResponse

from players.models import Player

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def playersind(request):
    queryset_list = Player.objects.order_by('team', 'name')

    #Team
    if 'team' in request.GET:
        team = request.GET['team']
        if team:
            queryset_list = queryset_list.filter(team=team)

    #Name
    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            queryset_list = queryset_list.filter(name__icontains=name)

    context = {
        'players': queryset_list,
        'retain_values': request.GET
    }

    return render(request, 'players/players_search.html', context)
    

def playerstatind(request):
    return render(request, 'pages/playerstatind.html')

def playerplusesind(request):
    return render(request, 'pages/playerplusesind.html')
