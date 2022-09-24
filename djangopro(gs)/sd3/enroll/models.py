from django.db import models

# Create your models here.
class User(models.Model):
    # name = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    # For show single column of student table in admin panel
    # def __str__(self):
    #     return self.stu_name


"""
    Model Form Inheritance 70
"""
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)