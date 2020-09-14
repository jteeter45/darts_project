from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Playerstat


def index(request):
		playerstat = Playerstat.objects.order_by('week', 'team', 'player_name')

		paginator = Paginator(playerstat, 10)
		page = request.GET.get('page')
		paged_playerstat = paginator.get_page(page)

		context = {
			'playerstat': paged_playerstat,
			}

		return render(request, 'playerstat/playerstat.html', context)

def playerstat_search(request):
		queryset_list = Playerstat.objects.order_by('week', 'team', 'player_name')
		
		#Week
		if 'week' in request.GET:
			week = request.GET['week']
			if week:
				queryset_list = queryset_list.filter(week=week)

        #Team
		if 'team' in request.GET:
			team = request.GET['team']
			if team == "Alpha":
				teamGet = 2 
				#if team:
				queryset_list = queryset_list.filter(team=teamGet)

		context = {
			'playerstat': queryset_list,
			'retain_values': request.GET
		}

		return render(request, 'playerstat/playerstat_search.html', context)
