from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from .forms import LoginForm


urlpatterns = [
    # ---------------- 122 Customize Authentication ------------------
    # path('', views.homeTemplateView.as_view(), name='home'),
    path('', TemplateView.as_view(template_name='myapp/home.html'), name='home'),
    
    # path('accounts/profile/', views.ProfileTemplateView.as_view(), name='profile'),
    path('profile/', TemplateView.as_view(template_name='myapp/profile.html'), name='profile'),
    
    # path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html', authentication_form=LoginForm), name='login'),
    
    # path('logout/', auth_views.LogoutView.as_view(template_name='myapp/logout.html'), name='logout'),

    # path('change_password/', auth_views.PasswordChangeView.as_view(template_name='myapp/change_password.html', success_url='/change_password_done/'), name='change_password'),
    path('change_password_done/', auth_views.PasswordChangeDoneView.as_view(template_name='myapp/password_change_done.html'), name='change_password_done'),


    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('change_password/', views.MyPasswordChangeView.as_view(), name='change_password'),

]