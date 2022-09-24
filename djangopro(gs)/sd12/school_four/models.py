from django.db import models
from .managers import CustomManager

# Custom Model Manager 103
# Model Manager with Proxy Model

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()


class ProxyStudent(Student):
    students = CustomManager()
    class Meta:
        proxy = True
        ordering = ['name']