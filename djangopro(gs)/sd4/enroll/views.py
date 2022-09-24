from email import message
from django.shortcuts import render
from . import models
from . import forms
from django.contrib import messages

# Create your views here.

"""
    Messages Framework 71
"""
def regi(request):
    if request.method == 'POST':
        fm = forms.UserRegistration(request.POST)
        if fm.is_valid():
            # fm.save()
            
            # print(messages.get_level(request))
            messages.add_message(request, messages.SUCCESS, ' Your Account has been created.')
            messages.info(request, 'Know You can login.')

            messages.add_message(request, messages.ERROR, ' Something is Wrong. ')

            """
                for set level
            """
            messages.set_level(request,messages.DEBUG)
            print(messages.get_level(request))
            messages.debug(request, 'This is Debug')
    else:
        fm = forms.UserRegistration()
    return render(request, 'enroll/user.html', {'form': fm})