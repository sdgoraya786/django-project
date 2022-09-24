from django import views
from django.shortcuts import render, redirect
from .models import Resume
from .forms import ResumeForm
from django.views import View

# 4
class HomeView(View):
    def get(self, request):
        fm = ResumeForm()
        # 12
        candidates = Resume.objects.all()
        return render(request, 'myapp/resume.html', {'form':fm, 'candidates':candidates})
    
    # 9
    def post(self, request):
        fm = ResumeForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            # return render(request, 'myapp/resume.html', {'form':fm})
            return redirect('home')

# 13
class CandidateView(View):
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request, 'myapp/candidate.html', {'candidate':candidate})