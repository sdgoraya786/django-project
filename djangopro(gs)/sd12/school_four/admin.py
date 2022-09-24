from django.contrib import admin
from .models import Student, ProxyStudent

# Custom Model Manager 103
# Model Manager with Proxy Model

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll')

@admin.register(ProxyStudent)
class ProxyStudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll')
