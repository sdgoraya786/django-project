from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    address = models.TextField()
    phone = models.IntegerField()


    def __str__(self):
        return self.name