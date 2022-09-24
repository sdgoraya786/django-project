from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import CntactForm

# Base Class-based View - View* 108

# Function Based view
def myview(request):
    return HttpResponse('<h3>Function Based view</h3>')

# Class Based view
class MyView(View):
    name = 'SD'
    def get(self, request):
        # return HttpResponse('<h3>Class Based view - GET</h3>')
        return HttpResponse(self.name)

class MyChildView(MyView):
    def get(self, request):
        return HttpResponse(self.name)


#---------------------------------------------------#
# Function Based view
def homeview(request):
    return render(request, 'school/home.html')

# Class Based view
class homeclassview(View):
    def get(self, request):
        return render(request, 'school/home.html')



#---------------------------------------------------#
# Function Based view
def aboutfun(request):
    context = {
        'msg': 'Welcome to SD Goraya Function base view'
    }
    return render(request, 'school/adout.html', context)

# Class Based view
class adoutclassview(View):
    def get(self, request):
        context = {
            'msg': 'Welcome to SD Goraya Class base view'
        }
        return render(request, 'school/adout.html', context)



#---------------------------------------------------#
# Function Based view
def contactfun(request):
    if request.method == 'POST':
        fm = CntactForm(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['name'])
            return HttpResponse('Thanks for Submitted!')  
    else:
        fm = CntactForm()

    return render(request, 'school/contact.html', {'form': fm})

# Class Based view
class contactclassview(View):
    def post(self, request):
        fm = CntactForm(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['name'])
            # return HttpResponse('Thanks for Submitted!')    
        return render(request, 'school/contact.html', {'form': fm})

    def get(self, request):
        fm = CntactForm()
        return render(request, 'school/contact.html', {'form': fm})


#---------------------------------------------------#
# Function Based view
def newsfun(request, template_name):
    # template_name = 'school/news.html'
    context = {'info': 'Welcome to SD Goraya function base view'}
    return render(request, template_name, context)

# Class Based view
class newsclassview(View):
    # template_name = 'school/news.html'
    template_name = ''
    def get(self, request):
        context = {'info': 'Welcome to SD Goraya Class base view'}
        return render(request, self.template_name, context)
        # return render(request, template_name, context)