from django.contrib import admin
from .models import Song
# Register your models here.
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'song_name', 'song_duration', 'written_by']