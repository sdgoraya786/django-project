from django.core import validators
from django import forms
from . import models

"""
    Messages Framework 71
"""
class UserRegistration(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['name', 'email', 'password']
        labels = {'name':'Enter Name'}


        