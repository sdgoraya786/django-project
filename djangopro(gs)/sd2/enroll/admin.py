from django.contrib import admin
from .models import student
# Register your models here.

@admin.register(student)  # Best practic
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'stu_name', 'stu_email', 'stu_pass', 'stu_comment')
# admin.site.register(student, StudentAdmin)