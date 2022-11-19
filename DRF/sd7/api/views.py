from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

"""
Class Based APIView in Django REST Framework 13
Method 2.2

Nomarl api code > api view
"""

class StudentApi(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            stu = Student.objects.get(id=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'Student Added'}, status=status.HTTP_201_CREATED)
        return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'Complete Student data Updated'})
        return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk, format=None):
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'Partial Student data Updated'})
        return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        stu = Student.objects.get(id=pk)
        stu.delete()
        return Response({'success':'Student Deleted'})