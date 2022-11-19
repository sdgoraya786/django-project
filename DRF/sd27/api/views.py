from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .mypagination import MyPageNumberPagination

"""
Page Number Pagination in Django REST Framework 29
"""

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # for per view(localy)
    pagination_class = MyPageNumberPagination