from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

"""
Hyperlinked Model Serializer in Django REST Framework 33
"""

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer