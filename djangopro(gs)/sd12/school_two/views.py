from django.shortcuts import render
from .models import Student

# Custom Model Manager 103
# Modify The Initial QuerySet

def home(request):
    sdata = Student.objects.all()
    sdata1 = Student.students.all()
    data = {
        'students' : sdata1
    }
    return render(request, 'schoolt/home.html', data)