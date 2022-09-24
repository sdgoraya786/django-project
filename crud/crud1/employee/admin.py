from django.contrib import admin
from .models import *

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','email','address','phone')

admin.site.register(Employee,EmployeeAdmin)