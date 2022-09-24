from django.db import models

# Create your models here.

class Course(models.Model):
    course_img = models.CharField(max_length=50)
    course_title = models.CharField(max_length=50)
    course_desc = models.TextField()

class Course_Page_Title(models.Model):
    title = models.CharField(max_length=50)