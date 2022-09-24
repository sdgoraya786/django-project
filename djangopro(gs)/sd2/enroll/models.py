from django.db import models

# Create your models here.
class student(models.Model):
    stu_name = models.CharField(max_length=100)
    stu_email = models.EmailField(max_length=100)
    stu_pass = models.CharField(max_length=100)
    stu_comment = models.CharField(max_length=100, default='Not Available')

    
    # For show single column of student table in admin panel
    # def __str__(self):
    #     return self.stu_name
