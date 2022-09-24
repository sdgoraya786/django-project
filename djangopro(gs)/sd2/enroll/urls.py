from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.stu_info, name='studentInfo'),
    path('st2/', views.StuForms, name='studentForm'),
    path('st3/', views.FormData, name='studentForm2'),
    path('success/', views.ThankYou, name='success'),
    
    path('st4/', views.FormField, name='FormField'),

    path('st5/', views.SpecificFormField, name='SpecificFormField'),
    
    path('st6/', views.FullFormvalidating, name='FullFormvalidating'),

    path('st7/', views.BuiltinValidation, name='BuiltinValidation'),

    path('st8/', views.CustomValidators, name='CustomValidators'),

    path('st9/', views.MatchPasswordRePassword, name='MatchPasswordRePassword'),

    path('st10/', views.StyleFieldErrors, name='StyleFieldErrors'),

    path('st11/', views.DjangoFormCRUD, name='DjangoFormCRUD'),
]