from django.contrib import admin
from .models import Student, Teacher

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'roll_no', 'name',  'city', 'marks', 'division', 'admission_data_time', 'pass_date']

@admin.register(Teacher)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'emp_no', 'name',  'city', 'salary', 'join_date']