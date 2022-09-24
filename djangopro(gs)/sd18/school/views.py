from django.shortcuts import render
from .models import Student
from django.views.generic.list import ListView
 
# Create your views here.
# Generic Class Based View - Display View: ListView [Default template name] - 112
class StudentListView(ListView):
    model = Student

# Generic Class Based View - Display View: ListView [Change Template Name Suffix]
# class StudentListView(ListView):
#     model = Student
#     template_name_suffix = '_get'
#     ordering = ['name']

# Generic Class Based View - Display View: ListView [Custom Template Name]
# class StudentListView(ListView):
#     model = Student
#     template_name = 'school/student.html'
#     context_object_name = 'students' # Custom context key name


# Generic Class Based View - Display View: ListView [Custom Template Name]
# class StudentListView(ListView):
#     model = Student
#     template_name = 'school/student.html'
#     context_object_name = 'students' # Custom context key name

#     # Methods for filter
#     def get_queryset(self):
#         return Student.objects.filter(course='Python')

#     # Methods Context object(key) name
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["freshers"] = Student.objects.all().order_by('name')
#         return context
    
    # Dynamic Template Name 
    # def get_template_names(self):
    #     if self.request.COOKIES['user'] == 'maha':
    #         template_name = 'shool/m.html'
    #     else:
    #         template_name = self.template_name
    #     return [template_name]

    # def get_template_names(self):
    #     if self.request.user.is_superuser:
    #         template_name = 'shool/superuser.html'
    #     elif self.request.user.is_staff:
    #         template_name = 'shool/staff.html'
    #     else:
    #         template_name = self.template_name
    #     return [template_name]
    
    
        
    