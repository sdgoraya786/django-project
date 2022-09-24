from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def home2(request):
    print('I am Home2 view')
    return HttpResponse('This is Home2 page')

def excp(request):
    print('I am Excp view')
    a = 10/0
    return HttpResponse('This is Excp page')

def user_info(request):
    print('I am User Info view')
    context = {
        'name': 'SD Goraya'
    }
    return TemplateResponse(request, 'blog/user.html', context)


## Site Under Construction Django 95 ##
def home(request):
    return render(request, 'SiteUnderConstruction/home.html')
def about(request):
    return render(request, 'SiteUnderConstruction/about.html')
