from django.shortcuts import render
from .models import Student
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

# Create your views here.
# Generic Class Based View - Display View: DetailView [Default template name] - 113
# class StudentDetail(DetailView):
#     model = Student

# Generic Class Based View - Display View: DetailView [Custom template name and suffix] - 113
# class StudentDetail(DetailView):
#     model = Student
#     # template_name = 'school2/student.html' # only work for this
#     # context_object_name = 'stu' # Custom Context key name
#     pk_url_kwarg = 'id' # Default <int:pk> | Custom <int:id>



###########################################################################
# Generic Class Based View - Display View: ListView and DetailView - 113
class StudentList(ListView):
    model = Student

class StudentDetail(DetailView):
    model = Student

    # For Show all Students Data in Detail page
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["all_students"] = self.model.objects.all().order_by('name')
        context["all_students"] = self.model.objects.all()
        return context
    