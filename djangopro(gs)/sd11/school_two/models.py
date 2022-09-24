from django.db import models

# MultiTable Inheritance 102
class ExamCenter(models.Model):
    center_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class Student(ExamCenter):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
