from django.shortcuts import render

from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from .customauth import CustomAuthentication
from rest_framework.permissions import IsAuthenticated

"""
Custom Authentication in Django REST Framework 23
"""

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]