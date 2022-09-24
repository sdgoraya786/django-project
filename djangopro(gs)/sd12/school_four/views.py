from django.shortcuts import render
from .models import Student, ProxyStudent

# Custom Model Manager 103
# Model Manager with Proxy Model

def home(request):
    sdata = Student.objects.all()
    sdata1 = ProxyStudent.students.all()
    sdata2 = ProxyStudent.students.get_stu_roll_range(102, 104)
    data = {
        'students' : sdata
    }
    return render(request, 'schoolth/home.html', data)
