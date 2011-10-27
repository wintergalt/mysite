from songs.models import Song
from django.contrib import admin

class SongAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('title','pub_date','artist')
    list_filter= ['artist']
    search_fields = ['title']
    date_hierarchy = 'pub_date'
    
    
admin.site.register(Song, SongAdmin)