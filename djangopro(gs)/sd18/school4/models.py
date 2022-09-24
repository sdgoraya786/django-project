from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)

    # Redirect url after save data
    # def get_absolute_url(self):
    #     return reverse("addstudent")

    # Redirect url after save data and see data on this page
    def get_absolute_url(self):
        return reverse("sdetail", kwargs={"pk": self.pk})
    
    