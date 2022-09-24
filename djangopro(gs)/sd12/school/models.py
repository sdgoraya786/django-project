from django.db import models

# Change Manager Name 103
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()

    # objects = models.Manager() # By Default Manager name
    # students = models.Manager() # Custom Manager name
