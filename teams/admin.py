from django.contrib import admin
from .models import Team	

class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'abbrev', 'name', 'site')
    list_display_links = ('id', 'abbrev')
    search_fields = ('abbrev',)
    list_per_page = 3

admin.site.register(Team, TeamAdmin)
