from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

"""
GenericAPIView and Model Mixins in Django REST Framework 14
(GenericAPIView class extends REST framework's APIView class)
Method 3.1 of API Create [Better than previous, 1.1, 1.2, 2.1, 2.2]

Nomarl api code > api view > GenericAPIView and Model Mixins
"""

# class StudentList(ListModelMixin, GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# class StudentCreate(CreateModelMixin, GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class StudentRetrieve(RetrieveModelMixin, GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class StudentUpdate(UpdateModelMixin, GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

# class StudentDestroy(DestroyModelMixin, GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)



"""/////////////////////////////////////////////////////////////////////"""
# List, create Student API - PK not required
class LCStudentAPI(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# Retrieve, Update, Destroy Student API - PK required
class RUDStudentApi(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)