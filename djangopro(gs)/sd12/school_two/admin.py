from django.contrib import admin
from .models import Student

# Custom Model Manager 103
# Modify The Initial QuerySet

@admin.register(Student)
class NameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll')
