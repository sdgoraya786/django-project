from django.shortcuts import render
from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializer
from django.views.decorators.csrf import csrf_exempt

from django.views import View
from django.utils.decorators import method_decorator

"""
Validation in Django REST Framework 10
"""

@method_decorator(csrf_exempt, name='dispatch')
class StudentApi(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream) # py dict
        id = py_data.get('id', None)
        # print(id)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return JsonResponse(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream) # py dict
        serializer = StudentSerializer(data=py_data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success':'Student Added'})
        return JsonResponse({'error':serializer.errors})

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream) # py dict
        id = py_data.get('id')
        print(id)
        stu = Student.objects.get(id=id)
        print(stu)
        serializer = StudentSerializer(stu, data=py_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'success':'Student Updated'})
        return JsonResponse({'error':serializer.errors})

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        py_data = JSONParser().parse(stream) # py dict
        id = py_data.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        return JsonResponse({'success':'Student Deleted'})