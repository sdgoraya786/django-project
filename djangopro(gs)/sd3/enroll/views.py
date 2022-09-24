from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from . import forms


"""
    ModelForm 65
"""
def ModelFormCRUD(request):
    if request.method == 'POST':

        """ 
        for update data [provide instance] 
        """
        # pi = models.User.objects.get(pk=1)
        # fm = forms.UserRegistration(request.POST, instance=pi)
        # if fm.is_valid():
        #     fm.save()
        
        fm = forms.UserRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = models.User(name=nm, email=em, password=pw)
            # reg.save()

            """ 
                For Delete 
            """
            # reg = models.User(id=1)
            # reg.delete()
    else:
        fm = forms.UserRegistration()
    return render(request, 'enroll/forms.html', {'form': fm})



"""
    Dynamic URL 66
"""
def home(request, check):
    print(check)
    return render(request, 'enroll/home.html')
def allusers(request):
    return render(request, 'enroll/user.html')
def DynamicURL(request, id):
    data = {'id': id}
    return render(request, 'enroll/stu.html', data)
def SubDetails(request, id, subid):
    data = {'id': id,'subid':subid}
    return render(request, 'enroll/stu.html', data)

"""
    Custom Path Converters 67
"""
def year_archive(request, year):
    data = {'yr': year}
    return render(request, 'enroll/stu.html', data)


"""
    Selecting ModelForm Fields 69
"""
def ModelForm(request):
    fm = forms.ModelForm()
    return render(request, 'enroll/forms.html', {'form': fm})


"""
    Model Form Inheritance 70
"""
def student_form(request):
    if request.method == 'POST':
        fm = forms.StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = forms.StudentRegistration()
    return render(request, 'enroll/student.html', {'form': fm})

def teacher_form(request):
    if request.method == 'POST':
        fm = forms.TeacherRegistration(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = forms.TeacherRegistration()
    return render(request, 'enroll/teacher.html', {'form': fm})