from django.db import models
from django.forms import CharField, EmailField

# Create your models here.

class Contact(models.Model):
    contact_name = models.CharField(max_length=50)
    contact_email = models.EmailField(max_length=50)
    contact_messsage = models.TextField()
