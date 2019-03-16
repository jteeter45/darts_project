from django.contrib import admin
from .models import Schedule	

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'team_one', 'score_one', 'team_two', 'score_two', 'team_three', 'score_three', 'team_four', 'score_four', 'team_five', 'score_five', 'team_six', 'score_six', 'team_seven', 'score_seven', 'team_eight', 'score_eight', 'week')
    list_display_links = ('id', 'team_one', 'team_two')
    list_filter = ('week',)
    search_fields = ('team_one', 'team_two')
    list_per_page = 10
    
admin.site.register(Schedule, ScheduleAdmin)
