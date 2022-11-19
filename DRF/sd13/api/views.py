from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny, IsAdminUser

"""
Basic Authentication and Permission Class in Django REST Framework 18
and The default authentication schemes and permission policy may be set globally in setting.py
"""

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    ## Authenticat with username and password
    authentication_classes = [BasicAuthentication]
    ## Only register user
    # permission_classes = [IsAuthenticated]   
    permission_classes = [IsAdminUser]   

# for override global permissions and authentication
# class StudentModelViewSet2(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [AllowAny]