from django.db import models

# Create your models here.
class ExamCenter(models.Model):
    center_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class MyExamCenter(ExamCenter):
    class Meta:
        proxy = True
        # ordering = ['id']
        ordering = ['city']
