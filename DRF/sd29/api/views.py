from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .mypagination import MyCursorPagination

"""
Cursor Pagination in Django REST Framework 31
"""

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    # for per view(localy)
    pagination_class = MyCursorPagination