from django.contrib import admin
from .models import Standing	

class StandingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'wins', 'losses', 'week', 'team')
    list_display_links = ('id', 'week', 'team')
    list_filter = ('week', 'team')
    search_fields = ('week', 'team')
    list_per_page = 15
    
admin.site.register(Standing, StandingsAdmin)
