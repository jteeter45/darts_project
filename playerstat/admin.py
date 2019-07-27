from django.contrib import admin
from .models import Playerstat	
from django.db.models.expressions import RawSQL

#Fix ALL win/loss counter fields START
Playerstat.objects.filter(five_singles_wldnp = "W"). \
        update(five_singles_win=RawSQL( '1' , []))

Playerstat.objects.filter(five_singles_wldnp = "L"). \
        update(five_singles_loss=RawSQL( '1' , []))

Playerstat.objects.filter(cricket_singles_wldnp = "W"). \
        update(cricket_singles_win=RawSQL( '1' , []))

Playerstat.objects.filter(cricket_singles_wldnp = "L"). \
        update(cricket_singles_loss=RawSQL( '1' , []))

Playerstat.objects.filter(five_doubles_wldnp = "W"). \
        update(five_doubles_win=RawSQL( '1' , []))

Playerstat.objects.filter(five_doubles_wldnp = "L"). \
        update(five_doubles_loss=RawSQL( '1' , []))

Playerstat.objects.filter(cricket_doubles_wldnp = "W"). \
        update(cricket_doubles_win=RawSQL( '1' , []))

Playerstat.objects.filter(cricket_doubles_wldnp = "L"). \
        update(cricket_doubles_loss=RawSQL( '1' , []))

#Fix ALL win/loss counter fields END

#def update_fiveSinglesLoss:
    #Playerstat.objects.all(). \
        #update(playerstat=RawSQL('update playerstat_playerstat set five_singles_loss = 1 where five_singles_wldnp = "L";', []))
#def update_winloss(modeladmin, request, queryset):
    #if Playerstat.objects.filter(five_singles_wldnp= "W"):
        #queryset.update(five_singles_win=1)
#update_winloss.short_description = "Mark selected Playerstat records win-loss"

class PlayerstatAdmin(admin.ModelAdmin):
    list_display = ('id', 'player_name', 'five_singles_wldnp', 'cricket_singles_wldnp','five_doubles_wldnp', 'cricket_doubles_wldnp', 'week', 'team')
    #list_display = ('id', 'player_name', 'five_singles_wldnp', 'five_singles_win', 'five_singles_loss', 'cricket_singles_wldnp','cricket_singles_win', 'cricket_singles_loss', 'five_doubles_wldnp', 'five_doubles_win', 'five_doubles_loss',  'cricket_doubles_wldnp', 'cricket_doubles_win', 'cricket_doubles_loss', 'week', 'team')
    list_display_links = ('id', 'week', 'team', 'player_name')
    list_filter = ('week', 'team')
    search_fields = ('week', 'team', 'player_name')
    #actions = [update_fiveSinglesWin]
    #actions = [update_fiveSinglesLoss]
    list_per_page = 15
    
admin.site.register(Playerstat, PlayerstatAdmin)
