from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import LoginForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView

# Create your views here.
# class homeTemplateView(TemplateView):
#     template_name = "myapp/home.html"

# class ProfileTemplateView(TemplateView):
#     template_name = "myapp/profile.html"

class MyLoginView(LoginView):
    template_name='myapp/login.html'
    authentication_form=LoginForm

class MyLogoutView(LogoutView):
    template_name='myapp/logout.html'

class MyPasswordChangeView(PasswordChangeView):
    template_name='myapp/change_password.html'
    success_url='/change_password_done/'