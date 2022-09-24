from django.shortcuts import render,redirect
from .forms import StudentRegistration
from .models import Student
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# This function show all items
def home(request):
    fm = StudentRegistration()
    return render(request, "enroll2/add-show.html", {'forms':fm})

@csrf_exempt
def load_data(request):
    if request.method == 'POST':
        st_data = Student.objects.values()
        student_data = list(st_data)
        if student_data != []:
            return JsonResponse({'status':'True', 'student_data':student_data})
        else:
            return JsonResponse({'status':'False', 'student_data':'No Record Found.'})

# This function Add/Update items
# @csrf_exempt  # remove csrf protection
def save_data(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            id = request.POST.get('id')
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if (id == ''):
                data = Student(name=name, email=email, password=password)
            else:
                data = Student(id=id, name=name, email=email, password=password)
            data.save()
            return JsonResponse({'status':'True'})
        else:
            return JsonResponse({'status':'False'})

# This function will delete item
def delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        st_data = Student.objects.get(pk=id) # pk = primary key
        st_data.delete()
        return JsonResponse({'status':'True'})
    else:
        return JsonResponse({'status':'False'})


# This function will edit item
def edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('sid')
        student = Student.objects.get(pk=id)
        student_data = {'id':student.id, 'name': student.name, 'email':student.email, 'password':student.password}
        return JsonResponse(student_data)

# This function will update/edit item
def live_search_data(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        search_data = Student.objects.filter(name__icontains=search).values()
        student_data = list(search_data)
        if student_data != []:
            return JsonResponse({'status':'True', 'student_data':student_data})
        else:
            return JsonResponse({'status':'False', 'student_data':'No Match Found.'})
