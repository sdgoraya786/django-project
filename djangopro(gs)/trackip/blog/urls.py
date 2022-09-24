from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('user/dashboard/', views.dashboard, name='dashboard'),
    path('user/post/add/', views.add_post, name='addpost'),
    path('user/post/<int:id>/change/', views.update_post, name='updatepost'),
    path('user/post/<int:id>/delete/', views.delete_post, name='deletepost'),

    path('user/signup/', views.user_signup, name='signup'),
    path('user/login/', views.user_login, name='login'),
    path('user/logout/', views.user_logout, name='logout'),
]