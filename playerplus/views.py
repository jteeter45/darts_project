from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Playerplus

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

        
		context = {
			'playerplus': queryset_list,
			'retain_values': request.GET
		}

		return render(request, 'playerplus/playerplus_search.html', context)
