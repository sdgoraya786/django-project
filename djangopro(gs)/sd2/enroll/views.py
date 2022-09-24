from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import student
from . import forms as form
# import enroll.forms as form

# Create your views here.
def stu_info(request):
    # fm = form.StudentRegistration(auto_id=True, label_suffix='  ', initial={'first_name': 'Shahzad'})  # 47
    fm = form.StudentRegistration()
    # fm.order_fields(field_order=['email', 'name'])  # 48
    stuData = student.objects.all()
    data = {
        'stu' : stuData,
        'form': fm
    }
    return render(request, 'enroll/stu.html', data)

#####################
def StuForms(request):
    """--- Loop Form Fields ----"""
    # fm = form.StudentRegistration2()

    """---- Form Hidden Fields -----"""
    # fm = form.StudentRegistration3()

    """---- Form Field Argument 51 -----"""
    # fm = form.StudentRegistration4()
    # data = {'form': fm}
    # return render(request, 'enroll/forms.html', data)

    """---- Form Widgets 52 -----"""
    # fm = form.StudentRegistration5()
    # data = {'form': fm}
    # return render(request, 'enroll/forms.html', data)

    """---- Form using Method POST and CSRF Token 55 -----"""
    fm = form.StudentRegistration6()
    data = {'form': fm}
    return render(request, 'enroll/forms.html', data)

""" ///// //////////// ////// """
"""HttpResponseRedirect 57"""
def ThankYou(request):
    return render(request, 'enroll/success.html')
""" ///// Get Form Data and Validate Data 56 ////// """
def FormData(request):
    if request.method == 'POST':
        fm = form.PostFormData(request.POST)
        if fm.is_valid():
            # print(request.POST['name']) # this method not use
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            print(name)
            print(email)
            return HttpResponseRedirect('/enroll/success/')
            # return render(request, 'enroll/success.html', {'nm': name})
    else:
        fm = form.PostFormData()
    return render(request, 'enroll/forms2.html', {'form': fm})

""" ///// //////////// ////// """
""" ///// Form Fields 58 ////// """
def FormField(request):
    if request.method == 'POST':
        fm = form.FormField(request.POST)
        if fm.is_valid():
            print('Name:-',fm.cleaned_data['name'])
            print('Email:-',fm.cleaned_data['email'])
            print('Roll:-',fm.cleaned_data['roll'])
            print('Price:-',fm.cleaned_data['price'])
            print('Rate:-',fm.cleaned_data['rate'])
            print('Comment:-',fm.cleaned_data['comment'])
            print('Website:-',fm.cleaned_data['website'])
            print('Password:-',fm.cleaned_data['password'])
            print('description:-',fm.cleaned_data['description'])
            print('feedback:-',fm.cleaned_data['feedback'])
            print('notes:-',fm.cleaned_data['notes'])
            print('aggree:-',fm.cleaned_data['agree'])
    else:
        fm = form.FormField()
    return render(request, 'enroll/forms2.html', {'form': fm})


""" ///// //////////// ////// """
""" ///// Custom cleaning and Validating Specific Form Field 59 ////// """
def SpecificFormField(request):
    if request.method == 'POST':
        fm = form.CleanValidation(request.POST)
        if fm.is_valid():
            print('Name:-',fm.cleaned_data['name'])
            print('Email:-',fm.cleaned_data['email'])
            print('Password:-',fm.cleaned_data['password'])
    else:
        fm = form.CleanValidation()
    return render(request, 'enroll/forms2.html', {'form': fm})

""" ///// //////////// ////// """
""" ///// Custom validating Complete Django Form at Once 60 ////// """
def FullFormvalidating(request):
    if request.method == 'POST':
        fm = form.ValidationFullForm(request.POST)
        if fm.is_valid():
            print('Name:-',fm.cleaned_data['name'])
            print('Email:-',fm.cleaned_data['email'])
            # print('Password:-',fm.cleaned_data['password'])
    else:
        fm = form.ValidationFullForm()
    return render(request, 'enroll/forms2.html', {'form': fm})


""" ///// //////////// ////// """
""" ///// Built in Validators 61 ////// """
def BuiltinValidation(request):
    if request.method == 'POST':
        fm = form.BuiltinValidators(request.POST)
        if fm.is_valid():
            print('Name:-',fm.cleaned_data['name'])
            print('Email:-',fm.cleaned_data['email'])
    else:
        fm = form.BuiltinValidators()
    return render(request, 'enroll/forms2.html', {'form': fm})


""" ///// //////////// ////// """
""" ///// Custom Form Validators 61 ////// """
def CustomValidators(request):
    if request.method == 'POST':
        fm = form.CustomValidators(request.POST)
        if fm.is_valid():
            print('Name:-',fm.cleaned_data['name'])
            print('Email:-',fm.cleaned_data['email'])
    else:
        fm = form.CustomValidators()
    return render(request, 'enroll/forms2.html', {'form': fm})


""" ///// //////////// ////// """
""" ///// Match Password and Re Enter Password 62 ////// """
def MatchPasswordRePassword(request):
    if request.method == 'POST':
        fm = form.MatchPasswordRePassword(request.POST)
        if fm.is_valid():
            print('Password:-',fm.cleaned_data['password'])
            print('Again Password:-',fm.cleaned_data['again_password'])
    else:
        fm = form.MatchPasswordRePassword()
    return render(request, 'enroll/forms2.html', {'form': fm})


""" ///// //////////// ////// """
""" ///// Styling Django Form Errors and Field Error 63 ////// """
def StyleFieldErrors(request):
    if request.method == 'POST':
        fm = form.StyleFieldErrors(request.POST)
        if fm.is_valid():
            print('Name:-',fm.cleaned_data['name'])
            print('Email:-',fm.cleaned_data['email'])
            print('Password:-',fm.cleaned_data['password'])
    else:
        fm = form.StyleFieldErrors()
    return render(request, 'enroll/forms2.html', {'form': fm})


""" ///// //////////// ////// """
""" ///// Save Update and Delete Django Form(API) Data to/from Database 64 ////// """
def DjangoFormCRUD(request):
    if request.method == 'POST':
        fm = form.CRUD_DjangoForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            cmt = fm.cleaned_data['comment']
            """ For Insert data """
            reg = student(stu_name=nm, stu_email=em, stu_pass=pw, stu_comment=cmt)
            """ for update data [add id] """
            # reg = student(id=1, stu_name=nm, stu_email=em, stu_pass=pw, stu_comment=cmt)
            reg.save()
            """ For Delete """
            # reg = student(id=1)
            # reg.delete()
    else:
        fm = form.CRUD_DjangoForm()
    return render(request, 'enroll/forms2.html', {'form': fm})