from django.contrib import admin
from .models import ExamCenter, Student

# Register your models here.
@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ['id', 'center_name', 'city']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'examcenter_ptr_id', 'name', 'roll']
