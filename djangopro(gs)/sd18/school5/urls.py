from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentListView.as_view(), name='students'),
    path('student/<int:pk>/', views.StudentDetail.as_view(), name='studentdetail'),

    path('student/add/', views.StudentCreateView.as_view(), name='addstudent'),
    path('student/<int:pk>/change/', views.StudentUpdateView.as_view(), name='updatestudent'),
    path('student/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='deletestudent'),

]