from django.db import models

# Create your models here.

class Student(models.Model):
    roll_no = models.IntegerField(unique=True, null=False)
    name = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    marks = models.IntegerField()
    division = models.CharField(max_length=70, null=True, default=None)  #97
    pass_date = models.DateField()
    admission_data_time = models.DateTimeField(null=True, default=None)  # 98

    def __str__(self):
        return self.name

class Teacher(models.Model):
    emp_no = models.IntegerField(unique=True, null=False)
    name = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    salary = models.IntegerField()
    join_date = models.DateField()

    def __str__(self):
        return self.name

