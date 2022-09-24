# from cProfile import label
# from dataclasses import field
# from distutils.log import error
# from tkinter import Widget
from django.core import validators
from django import forms
from . import models

"""
    ModelForm 65
"""
class UserRegistration(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput, min_length=6)
    # name = forms.CharField(min_length=6)
    class Meta:
        model = models.User
        fields = ['name', 'email', 'password']
        labels = {'name':'Enter Name'}
        # help_texts = {'name':'Enter Your Full Name Here...'}
        error_messages = {
            'name': {'required': 'Please Enter Your Name'},
            'email': {'invalid': 'Please Enter a valid email address'},
            'password': {'required': 'Please Enter Your Password'}
        }
        widgets = {
            'password': forms.PasswordInput,
            'name': forms.TextInput(attrs={'class':'myclass','placeholder':'Your Name'})
        }


"""
    Selecting ModelForm Fields 69
"""
class ModelForm(forms.ModelForm):
    class Meta:
        model = models.User
        # fields = ['name', 'email', 'password']
        fields = '__all__'
        # exclude = ['name']  # list
        # exclude = ('name',)    # tuple


"""
    Model Form Inheritance 70
"""
class StudentRegistration(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ['student_name', 'email', 'password']
class TeacherRegistration(StudentRegistration):
    class Meta(StudentRegistration.Meta):
        fields = ['teacher_name', 'email', 'password']


        