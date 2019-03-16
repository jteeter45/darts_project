from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Player

def index(request):
		players = Player.objects.order_by('team', 'name')

		paginator = Paginator(players, 10)
		page = request.GET.get('page')
		paged_players = paginator.get_page(page)

		context = {
			'players': paged_players,
        }

		return render(request, 'players/players.html', context)

def players_search(request):
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
