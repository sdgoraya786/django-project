from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets

"""
Model View Set in Django REST Framework 17
"""

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

"""
Ready Only Model View Set in Django REST Framework 17
"""

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    