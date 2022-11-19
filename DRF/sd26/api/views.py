from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

"""
Search Filter in Django REST Framework 27
"""

# class StudentList(ListAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     filter_backends = [SearchFilter]
#     search_fields = ['^city']

"""
Ordering Filter in Django REST Framework 28
"""

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['^city']
    ordering_fields = ['name']
    