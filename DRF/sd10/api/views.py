from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView

"""
Concrete View Class in Django REST Framework 15
Method 3.2 of API Create [Better than previous, 1.1, 1.2, 2.1, 2.2, 3.1]

Nomarl api code > api view > GenericAPIView and Model Mixins > Concrete View Class  --- for api
"""

# List and Create
class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Retrieve, Update and Destroy
class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer