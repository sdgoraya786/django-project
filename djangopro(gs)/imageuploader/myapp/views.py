from django.shortcuts import render
from .models import Image
from .forms import ImageForm
# Create your views here.
def home(request):
    img = Image.objects.all()
    if request.method == 'POST':
        fm = ImageForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
    fm = ImageForm()
    return render(request, 'myapp/home.html', {'img':img,'form':fm})