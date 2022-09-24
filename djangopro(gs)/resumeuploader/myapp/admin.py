from django.contrib import admin
from .models import Resume

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id','name','dob','gender','locality','state','city','pin','moblie','email','job_city','profile_image','upload_cv']

