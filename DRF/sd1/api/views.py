from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer

"""
Serializer and Serializertion in Django REST Framework
"""

# Model Object - Single Data
def student_detail(request,pk):
    stu = Student.objects.get(id = pk)
    # print('obj > ' ,stu)
    serializer = StudentSerializer(stu)
    # print('py_data > ' ,serializer)
    # print('py_Dict > ' ,serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data) # for dict objects

# Query Set - All Data
def student_list(request):
    stu = Student.objects.all()
    # print('obj > ' ,stu)
    serializer = StudentSerializer(stu, many=True)
    # print('py_data > ' ,serializer)
    # print('py_Dict > ' ,serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False) # for non-dict objects