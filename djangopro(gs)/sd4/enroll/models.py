from django.db import models

# Create your models here.
"""
    Messages Framework 71
"""
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)