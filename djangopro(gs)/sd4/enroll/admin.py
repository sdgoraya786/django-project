from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.User)  # Best practic
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')