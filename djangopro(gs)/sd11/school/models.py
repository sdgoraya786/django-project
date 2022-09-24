from django.db import models

# Abstract Base Class 102
class CommenInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date = models.DateField()
    class Meta:
        abstract = True

class Student(CommenInfo):
    fees = models.IntegerField()
    date = None

class Teacher(CommenInfo):
    salary = models.IntegerField()

class Contractor(CommenInfo):
    payment = models.IntegerField()
    date = models.DateTimeField()
