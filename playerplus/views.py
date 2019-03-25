from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Playerplus
from .choices import name_choices

def index(request):
		playerplus = Playerplus.objects.order_by('week', 'team', 'player_name')

		paginator = Paginator(playerplus, 10)
		page = request.GET.get('page')
		paged_playerplus = paginator.get_page(page)

		context = {
			'playerplus': paged_playerplus,
        }

		return render(request, 'playerplus/playerplus.html', context)

def playerplus_search(request):
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
				queryset_list = queryset_list.filter(player_name__icontains=player_name)

		context = {
			'name_choices': name_choices,
			'playerplus': queryset_list,
			'retain_values': request.GET
		}

		return render(request, 'playerplus/playerplus_search.html', context)
