from django.shortcuts import render,redirect
from .forms import StudentRegistration
from .models import Student
from django.views.generic.base import TemplateView, RedirectView, View

# Create your views here.

# This Class will add new item and show all items
class UserAddShowView(TemplateView):
    template_name = 'enroll/add-show.html'
    # for get request - show all data and form
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentRegistration()
        st_data = Student.objects.all()
        context = {'forms':fm, 'st_data':st_data}
        return context
    
    def post(self, request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            data = Student(name=name, email=email, password=password)
            data.save()
            return redirect('/')


# This Class will update/edit item
class UserUpdateView(View):
    def get(self, request, id):
        st_id = Student.objects.get(pk=id)
        fm = StudentRegistration(instance=st_id)
        return render(request, "enroll/update.html", {'forms':fm})

    def post(self, request, id):
        st_data = Student.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=st_data)
        if fm.is_valid():
            fm.save()
        return redirect('/')

# class UserUpdateView(TemplateView):
#     template_name = 'enroll/update.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         st_data = Student.objects.get(pk=kwargs['id'])
#         fm = StudentRegistration(instance=st_data)
#         context["forms"] = fm
#         return context
    
#     def post(self, request, **kwargs):
#         st_data = Student.objects.get(pk=kwargs['id'])
#         fm = StudentRegistration(request.POST, instance=st_data)
#         if fm.is_valid():
#             fm.save()
#         return redirect('/')


# This Class will delete item
class UserDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        Student.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)