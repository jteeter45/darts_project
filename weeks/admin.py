from django.contrib import admin
from .models import Week	

class WeekAdmin(admin.ModelAdmin):
    list_display = ('id', 'week_char', 'week_date')
    list_display_links = ('id', 'week_char')
    search_fields = ('week_char',)
    list_per_page = 3

admin.site.register(Week, WeekAdmin)
