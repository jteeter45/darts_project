from django.contrib import admin
from .models import Player	

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'team')
    list_display_links = ('id', 'name')
    list_filter = ('team',)
    search_fields = ('name',)
    list_per_page = 10
    
admin.site.register(Player, PlayerAdmin)
