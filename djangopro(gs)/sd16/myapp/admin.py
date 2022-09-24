from django.contrib import admin
from .models import Page, Post, Song
# Register your models here.

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['page_name','page_cat', 'page_publish_date', 'user', 'user_id']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'post_title', 'post_cat', 'post_publish_date']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['id', 'song_name', 'song_duration', 'written_by']