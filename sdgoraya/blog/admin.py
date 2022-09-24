from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE
# IntegratingTinymce editor(3)
from .forms import *

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title','blog_img','blog_desc')
    # IntegratingTinymce editor(4)
    form = BlogAdminForm

admin.site.register(Blog,BlogAdmin)


class BlogPageTitleAdmin(admin.ModelAdmin):
    list_display = ['blog_page_title']
admin.site.register(PageTitle,BlogPageTitleAdmin)
