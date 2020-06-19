from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Sum
from .models import Standing

def index(request):
		standings = Standing.objects.order_by('week', 'team')

		paginator = Paginator(standings, 10)
		page = request.GET.get('page')
		paged_standings = paginator.get_page(page)

		context = {
			'standings': paged_standings,
        }

		return render(request, 'standings/standings.html', context)

def standings_search(request):
		#queryset_list = Standing.objects.order_by('week', 'team')

		queryset_list = Standing.objects.values('team', 'week').order_by('-wins').annotate(wins=Sum('wins'),losses=Sum('losses'))

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
			'standings': queryset_list,
			'retain_values': request.GET
		}

		return render(request, 'standings/standings_search.html', context)
