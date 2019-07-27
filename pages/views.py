from django.shortcuts import render
from django.http import HttpResponse

from players.models import Player
from playerstat.models import Playerstat
from playerstat.choices import name_choices
from playerplus.models import Playerplus
from playerplus.choices import name_choices
from standings.models import Standing
from django.db.models import Sum

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
        'playersind': queryset_list,
        'retain_values': request.GET
    }

    return render(request, 'pages/playersind.html', context)

def playerstatind(request):
    queryset_list = Playerstat.objects.order_by('week', 'team', 'player_name')

    #Week
    if 'week' in request.GET:
        week = request.GET['week']
        if week:
            queryset_list = queryset_list.filter(week=week)

    #Team
    if 'team' in request.GET:
        team = request.GET['team']
        if team:
            queryset_list = queryset_list.filter(team=team)

    #Player_name
    if 'player_name' in request.GET:
        player_name = request.GET['player_name']
        if player_name:
            queryset_list = queryset_list.filter(player_name__icontains=name)

    context = {
        'name_choices': name_choices,
        'playerstatind': queryset_list,
        'retain_values': request.GET
    }

    return render(request, 'pages/playerstatind.html', context)   


def playerplusind(request):
    queryset_list = Playerplus.objects.order_by('week', 'team', 'player_name')

    #Week
    if 'week' in request.GET:
        week = request.GET['week']
        if week:
            queryset_list = queryset_list.filter(week=week)

    #Team
    if 'team' in request.GET:
        team = request.GET['team']
        if team:
            queryset_list = queryset_list.filter(team=team)

    #Player_name
    if 'player_name' in request.GET:
        player_name = request.GET['player_name']
        if player_name:
            queryset_list = queryset_list.filter(player_name__icontains=name)

    context = {
        'name_choices': name_choices,
        'playerplusind': queryset_list,
        'retain_values': request.GET
    }

    return render(request, 'pages/playerplusind.html', context) 

def standingsind(request):
    queryset_list = Standing.objects.values('team').order_by('-wins').annotate(wins=Sum('wins'),losses=Sum('losses'))

    #queryset_list = Standing.objects.order_by('week', 'team')
            
    #Week
    if 'week' in request.GET:
        week = request.GET['week']
        if week:
            queryset_list = queryset_list.filter(week=week)

    #Team
    if 'team' in request.GET:
        team = request.GET['team']
        if team:
            queryset_list = queryset_list.filter(team=team)


    context = {
        'standingsind': queryset_list,
        'retain_values': request.GET
    }

    return render(request, 'pages/standingsind.html', context)

def read_file(request):
    f = open('./darts_report.txt', 'r')
    file_content = f.read()
    f.close()
    return HttpResponse(file_content, content_type="text/plain")
