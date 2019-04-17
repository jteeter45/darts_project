from django.contrib import admin
from .models import Playerstat	

class PlayerstatAdmin(admin.ModelAdmin):
    list_display = ('id', 'player_name', 'five_singles_wldnp', 'cricket_singles_wldnp','five_doubles_wldnp', 'cricket_doubles_wldnp', 'week', 'team')
    #list_display = ('id', 'player_name', 'five_singles_wldnp', 'five_singles_win', 'five_singles_loss', 'cricket_singles_wldnp','cricket_singles_win', 'cricket_singles_loss', 'five_doubles_wldnp', 'five_doubles_win', 'five_doubles_loss',  'cricket_doubles_wldnp', 'cricket_doubles_win', 'cricket_doubles_loss', 'week', 'team')
    list_display_links = ('id', 'week', 'team', 'player_name')
    list_filter = ('week', 'team')
    search_fields = ('week', 'team', 'player_name')
    list_per_page = 15
    
admin.site.register(Playerstat, PlayerstatAdmin)
