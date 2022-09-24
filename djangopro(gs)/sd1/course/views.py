from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def leran_django(request):
    data = {
        'data' : 'MR.SD GORAYA'
    }
    return render(request, 'course/info.html', data)