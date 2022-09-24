from django.db import models
from .managers import CustomManager

# Custom Model Manager 103
# Add Extra Manager Methods

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()

    objects = models.Manager()
    students = CustomManager()