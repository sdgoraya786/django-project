from unicodedata import name
from django.shortcuts import render,redirect
from employee.models import Employee

# Read,edit.delete emp
def home(request):
    emp = Employee.objects.all()
    context = {
        'empdata': emp
    }
    return render(request, "index.html",context)

# Add emp
def add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employee(
            name= name,
            email= email,
            address= address,
            phone= phone
        )
        emp.save()
        return redirect('home')
    return render(request, "index.html")

# Edit emp
# def edit(request):
#     emp = Employee.objects.all()
#     context = {
#         'empdata': emp
#     }
#     return render(request, "index.html",context)

# Update emp
def update(request,id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employee(
            id = id,
            name = name,
            email = email,
            address = address,
            phone = phone
        )
        emp.save()
        return redirect('home')
    # return render(request, "index.html")

def delete(request,id):
    if request.method == "POST":
        emp = Employee.objects.filter(id = id).delete()
        return redirect('home')
    # return render(request, "index.html")