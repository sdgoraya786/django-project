from django.shortcuts import render,redirect
from .forms import StudentRegistration
from .models import Student

# Create your views here.

# This function will add new item and show all items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)

        # /// method 1 for save data ///
        # if fm.is_valid():
        #     fm.save()
        
        # /// method 2 for save data ///
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            data = Student(name=name, email=email, password=password)
            data.save()
            # for empty form after adding data
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    
    st_data = Student.objects.all()
    return render(request, "enroll/add-show.html", {'forms':fm, 'st_data':st_data})

# This function will delete item
def delete(request, id):
    if request.method == 'POST':
        st_data = Student.objects.get(pk=id) # pk = primary key
        st_data.delete()
        return redirect('/')

# This function will update/edit item
def update(request, id):
    msg = ''
    if request.method == 'POST':
        st_id = Student.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=st_id)
        if fm.is_valid():
            fm.save()
        # return redirect('/')
        msg = 'Student Information Updated'
    else:
        st_id = Student.objects.get(pk=id)
        fm = StudentRegistration(instance=st_id)

    return render(request, "enroll/update.html", {'forms':fm,'msg':msg})