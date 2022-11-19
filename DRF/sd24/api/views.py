from this import s
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView

"""
Filtering and django filter in Django REST Framework 26
"""

class StudentList(ListAPIView):
    # queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # filter
    def get_queryset(self):
        print(self.request.query_params)
        user = self.request.user
        return Student.objects.filter(passby=user)
    