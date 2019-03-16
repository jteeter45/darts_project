from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Schedule

def index(request):
		schedules = Schedule.objects.order_by('week')

		paginator = Paginator(schedules, 3)
		page = request.GET.get('page')
		paged_schedules = paginator.get_page(page)

		context = {
			'schedules': paged_schedules,
        }

		return render(request, 'schedules/schedules.html', context)
