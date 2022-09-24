from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Post
from django.utils.translation import gettext_lazy as _

# User Registration Form
class SignUpForm(UserCreationForm):
    password2 = forms.CharField(label='Password (again)',widget=forms.PasswordInput,help_text='Enter the same password as before, for verification.')

# Login User Form
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"autofocus": True, 'class':'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'class':'form-control'}),
    )    

# Add New Post Form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'desc']
        labels = {'title':'Title', 'desc':'Description'}
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}), 
            'desc': forms.Textarea(attrs={'class':'form-control','cols':40, 'rows':5})
        }