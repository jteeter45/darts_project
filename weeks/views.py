from django.shortcuts import render
from django.http import HttpResponse

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Week

def index(request):
	weeks = Week.objects.order_by('week_date')

	paginator = Paginator(weeks, 3)
	page = request.GET.get('page')
	paged_weeks = paginator.get_page(page)

	context = {
		'weeks': paged_weeks,
	}

	return render(request, 'weeks/weeks.html', context)
