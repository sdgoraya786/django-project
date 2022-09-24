import email
from email import message
from logging import PlaceHolder
from tkinter.tix import Form
from unicodedata import name


from django import forms

class usersForm(forms.Form):
    name = forms.CharField(label='', required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    message = forms.ChoiceField(widget=forms.Textarea(attrs={'class':'form-control'}))