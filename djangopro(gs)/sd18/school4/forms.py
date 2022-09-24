from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['roll', 'name', 'course']
        widgets = {
            'roll': forms.NumberInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'course': forms.TextInput(attrs={'class':'form-control'}),
            # 'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }