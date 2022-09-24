from django.shortcuts import render
from .models import Student

# Custom Model Manager 103
# Add Extra Manager Methods

def home(request):
    sdata = Student.objects.all()
    sdata1 = Student.students.get_stu_roll_range(102, 104)
    data = {
        'students' : sdata1
    }
    return render(request, 'schoolth/home.html', data)
