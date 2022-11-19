from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

"""
Token Authentication in Django REST Framework 22
"""

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer