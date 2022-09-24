# from codecs import register
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

    # Redirect url after updata data on student detail  page
    def get_absolute_url(self):
        return reverse("studentdetail", kwargs={"pk": self.pk})

    # for get model name m1
    # def get_model_name(self):
    #     return self.__class__.__name__
