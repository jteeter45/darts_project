from django.shortcuts import render
from django.http import HttpResponse

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Team

def index(request):
	teams = Team.objects.order_by('id')

	paginator = Paginator(teams,12)
	page = request.GET.get('page')
	paged_teams = paginator.get_page(page)

	context = {
		'teams': paged_teams,
	}

	return render(request, 'teams/teams.html', context)
