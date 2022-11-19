from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from .serializer import StudentSerializer
from django.views.decorators.csrf import csrf_exempt

"""
DeSerialization and Insert Data Django REST Framework
"""

# for bypass csrf token
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body
        print('JD > ',json_data)
        stream = io.BytesIO(json_data)
        print('Stream > ',stream)
        py_data = JSONParser().parse(stream)
        print('PyD > ', py_data)
        serializer = StudentSerializer(data=py_data)
        print('Serializer > ',serializer)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data Inserted!'}
            j_data = JSONRenderer().render(res)
            return HttpResponse(j_data, content_type='application/json')
        
        j_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(j_data, content_type='application/json')

