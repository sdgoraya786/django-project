from django.urls import path
from . import views

urlpatterns = [
    # path('', views.TemplateView.as_view(template_name='school2/home.html'), name='home'),

    # path('', views.HomeTemplateView.as_view(), name='home'),

    # path('', views.HomeTemplateView.as_view(extra_context={'course':'Python'}), name='home'),
    
    # path('about/<int:roll>', views.HomeTemplateView.as_view(), name='about'),
    path('about/<course>/', views.HomeTemplateView.as_view(), name='about'),
    #-----------------------------------------#
    #-----------------------------------------#
]