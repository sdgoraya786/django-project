from tkinter import N, Widget
from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField


# Create your models here.

class Blog(models.Model):
    blog_img = models.FileField(upload_to="blog/", max_length=255, null=True, default=None)
    blog_title = models.CharField(max_length=50)
    blog_slug = AutoSlugField(populate_from='blog_title', unique=True, null=True, default=None)
    # blog_desc = HTMLField()
    # IntegratingTinymce editor(1)
    blog_desc = models.TextField()

class PageTitle(models.Model):
    blog_page_title = models.CharField(max_length=50)

def __str__(self): 
    return self.blog_title