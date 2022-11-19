from django.shortcuts import render
from .models import Student
from rest_framework.response import Response
from .serializers import StudentSerializer
from rest_framework import status, viewsets

"""
ViewSet in Django REST Framework 16
"""

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        print("*************List***************")
        print('Basename: ',self.basename)
        print('Action: ',self.action)
        print('Detail: ',self.detail)
        print('Suffix: ',self.suffix)
        print('Name: ',self.name)
        print('Description: ',self.description)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        print("*************Retrieve***************")
        print('Basename: ',self.basename)
        print('Action: ',self.action)
        print('Detail: ',self.detail)
        print('Suffix: ',self.suffix)
        print('Name: ',self.name)
        print('Description: ',self.description)
        if pk is not None:
            stu = Student.objects.get(id = pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        print("*************Create***************")
        print('Basename: ',self.basename)
        print('Action: ',self.action)
        print('Detail: ',self.detail)
        print('Suffix: ',self.suffix)
        print('Name: ',self.name)
        print('Description: ',self.description)
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'Student Added'}, status=status.HTTP_201_CREATED)
        return Response({'error':serializer.error}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        print("*************Update***************")
        print('Basename: ',self.basename)
        print('Action: ',self.action)
        print('Detail: ',self.detail)
        print('Suffix: ',self.suffix)
        print('Name: ',self.name)
        print('Description: ',self.description)
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'Complete Student data Updated'})
        return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk):
        print("*************Partial Update***************")
        print('Basename: ',self.basename)
        print('Action: ',self.action)
        print('Detail: ',self.detail)
        print('Suffix: ',self.suffix)
        print('Name: ',self.name)
        print('Description: ',self.description)
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success':'Partial Student data Updated'})
        return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        print("*************Destroy***************")
        print('Basename: ',self.basename)
        print('Action: ',self.action)
        print('Detail: ',self.detail)
        print('Suffix: ',self.suffix)
        print('Name: ',self.name)
        print('Description: ',self.description)
        stu = Student.objects.get(id=pk)
        stu.delete()
        return Response({'success':'Student Deleted'})
