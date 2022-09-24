from django.urls import path
from . import views

urlpatterns = [
    path('', views.TemplateView.as_view(template_name='school3/home.html'), name='home'),
    path('home/', views.RedirectView.as_view(url='/'), name='home2'),

    # path('index/', views.RedirectView.as_view(url='/'), name='index'),
    path('index/', views.RedirectView.as_view(pattern_name='home2'), name='index'),
    
    # path('sd/', views.RedirectView.as_view(url='https://sdgoraya.pythonanywhere.com'), name='sd'),
    path('sd/', views.SDRedirectView.as_view(), name='sd'),

    path('home/<int:pk>/', views.SDGRedirectView.as_view(), name='home3'),
    path('roll/<int:pk>/', views.TemplateView.as_view(template_name='school3/home.html'), name='mindex'),
    # path('roll/<int:pk>/', views.HomeTemplateView.as_view(template_name='school3/home.html'), name='mindex'),
    #-----------------------------------------#
    #-----------------------------------------#
]