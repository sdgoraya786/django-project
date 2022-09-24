from django.urls import path
from . import views

urlpatterns = [
    path('singup/', views.sign_up, name='singup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('edit/', views.user_profileedit, name='editprofile'),
    path('<int:id>/change/', views.user_detail, name='userdetail'),
    path('password_change/', views.user_ChangePassword, name='changepassword'),
    path('password/', views.user_ChangePassword2, name='password'),
]