from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            'roll': forms.NumberInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'course': forms.TextInput(attrs={'class':'form-control'}),
            # 'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }