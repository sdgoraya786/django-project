from itertools import count
from django.shortcuts import render
from .models import Student
from django import forms
from .forms import StudentForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
# Generic Class Based View - Editing View: UpdateView - 116

# --StudentCreate--#
# class StudentCreateView(CreateView):
#     model = Student
#     fields = ['roll', 'name', 'course']
#     success_url = '/student/add/'

#     # add class for css in form fields
#     def get_form(self):
#         form = super().get_form()
#         form.fields['roll'].widget = forms.NumberInput(attrs={'class':'form-control'})
#         form.fields['name'].widget = forms.TextInput(attrs={'class':'form-control'})
#         form.fields['course'].widget = forms.TextInput(attrs={'class':'form-control'})
#         # form.fields['password'].widget = forms.PasswordInput(attrs={'class':'form-control'})
#         return form

# --StudentList--#
class StudentListView(ListView):
    model = Student

# --StudentDetails--#
class StudentDetail(DetailView):
    model = Student
    # --StudentList in Detail page--#
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_students"] = self.model.objects.all()
        return context

# --StudentUpdate --#
# class StudentUpdateView(UpdateView):
#     model = Student
#     fields = ['roll', 'name', 'course']

#     # add class for css in form fields
#     def get_form(self):
#         form = super().get_form()
#         form.fields['roll'].widget = forms.NumberInput(attrs={'class':'form-control'})
#         form.fields['name'].widget = forms.TextInput(attrs={'class':'form-control'})
#         form.fields['course'].widget = forms.TextInput(attrs={'class':'form-control'})
#         # form.fields['password'].widget = forms.PasswordInput(attrs={'class':'form-control'})
#         return form


#############################################################
# Use Model form in create and update for add classes
# --StudentCreate--#
class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'school5/student_form.html'
    success_url = '/student/add/'

# --StudentUpdate --#
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'school5/student_form.html'

# --DeleteView 117 --#
class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/'  # TemplateView bna kr os page pr b redirect krwa sakty hen
    # template_name = 'school5/confirm_delete.html'

    # for len of deleted Records
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["len_stu"] = len(kwargs)
        return context
    
    