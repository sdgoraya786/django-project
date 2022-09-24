from django.urls import path, register_converter
from . import views, converters

## """
    ##    Custom Path Converters 67
    ## """
register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('st1/', views.ModelFormCRUD, name='ModelFormCRUD'),


    ## """
    ##     Dynamic URL 66
    ## """
    path('', views.home, {'check':'OK'}, name='home'),
    path('user/', views.allusers, name='allusers'),

    ## """
    ##    this contain int ki type str ho gi , str, slug
    ## """
    # path('user/<id>/change', views.DynamicURL, name='DynamicURL'),

    ## """
    ##    only int
    ## """
    path('user/<int:id>/change', views.DynamicURL, name='DynamicURL'),
    path('user/<int:id>/<int:subid>/change', views.SubDetails, name='SubDetails'),


    ## """
    ##    Custom Path Converters 67
    ## """
    path('session/<yyyy:year>/', views.year_archive),


    ## """
    ##    Selecting ModelForm Fields 69
    ## """
    path('st2/', views.ModelForm),


    ## """
    ##    Model Form Inheritance 70
    ## """
    path('student/', views.student_form, name='student_form'),
    path('teacher/', views.teacher_form, name='teacher_form'),
]