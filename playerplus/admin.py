from django.contrib import admin
from .models import Playerplus	

class PlayerplusAdmin(admin.ModelAdmin):
    list_display = ('id', 'player_name', 'plus_one', 'ton_eighty', 'nine_hitter', 'mvp', 'high_out', 'six_bull', 'week', 'team')
    list_display_links = ('id', 'week', 'team', 'player_name')
    list_filter = ('week', 'team')
    search_fields = ('week', 'team', 'player_name')
    list_per_page = 15
    
admin.site.register(Playerplus, PlayerplusAdmin)
