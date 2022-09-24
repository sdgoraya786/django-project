from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import Student
from django import forms
from .forms import StudentForm

# Create your views here.
# Generic Class Based View - Editing View: CreateView - 115
# class StudentCreateView(CreateView):
#     model = Student
#     fields = ['roll', 'name', 'course']
#     # success_url = '/student/add/' # Redirect url after save data

#     # add class for css in form fields
#     def get_form(self):
#         form = super().get_form()
#         form.fields['roll'].widget = forms.NumberInput(attrs={'class':'form-control'})
#         form.fields['name'].widget = forms.TextInput(attrs={'class':'form-control'})
#         form.fields['course'].widget = forms.TextInput(attrs={'class':'form-control'})
#         # form.fields['password'].widget = forms.PasswordInput(attrs={'class':'form-control'})
#         return form


# 2nd Method - form with css class - 115
class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'school4/student_form.html'
#     # success_url = '/student/add/' # Redirect url after save data


# for Current add students details
class StudentDetailView(DetailView):
    model = Student

