from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.User)  # Best practic
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')
# admin.site.register(User, UserAdmin)

@admin.register(models.Student)  # Best practic
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_name', 'teacher_name', 'email', 'password')