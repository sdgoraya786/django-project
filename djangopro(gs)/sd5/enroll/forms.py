"""
     Inheriting UserCreationForm for more fields (p2)
"""
from tkinter.messagebox import YES
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

class SingUpForm(UserCreationForm):
    hlp = '<ul><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>'
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}),help_text=hlp)
    password2 = forms.CharField(label='Password (again)',widget=forms.PasswordInput(attrs={'class':'form-control'}),help_text='Enter the same password as before, for verification.')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {'email':'Email'}
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}), 
            'first_name': forms.TextInput(attrs={'class':'form-control'}), 
            'last_name': forms.TextInput(attrs={'class':'form-control'}), 
            'email': forms.EmailInput(attrs={'class':'form-control'})
        }

"""
    Profile using UserChangeForm 77
    User Profile
"""
class EditUserProfileForm(UserChangeForm):
    # password = 
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login']
        labels = {'email':'Email'}

"""
    Profile using UserChangeForm
    Admin Profile 78
"""
class EditAdminProfileForm(UserChangeForm):
    # password = 
    class Meta:
        model = User
        fields = '__all__'
        labels = {'email':'Email'}