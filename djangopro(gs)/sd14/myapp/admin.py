from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'post_title', 'post_cat', 'post_publish_date']
