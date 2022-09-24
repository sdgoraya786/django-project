from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fees_py(request):
    data = {
        'course_name': 'Python',
        'fees': 2000
    }
    return render(request, 'fees/info.html', data)

def fees_django(request):
    data = {
        'course_name': 'Django',
        'fees': 3000
    }
    return render(request, 'fees/info.html', data)

def fees_php(request):
    data = {
        'course_name': 'PHP',
        'fees': 4000
    }
    return render(request, 'fees/info.html', data)