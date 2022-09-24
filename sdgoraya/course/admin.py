from django.contrib import admin
from course.models import Course,Course_Page_Title
# from course.models import Course_Page_Title

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_img','course_title','course_desc')
admin.site.register(Course,CourseAdmin)

class CoursePageTitleAdmin(admin.ModelAdmin):
    list_display = ['title']
admin.site.register(Course_Page_Title,CoursePageTitleAdmin)