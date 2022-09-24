from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.StudentCreateView.as_view(), name='addstudent'),
    path('<int:pk>/detail/', views.StudentDetailView.as_view(), name='sdetail'),

]