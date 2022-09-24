# IntegratingTinymce editor(2)
from django import forms
from .models import *

class BlogAdminForm(forms.ModelForm): 
    blog_desc = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"})) 
    
class Meta: 
    model = Blog 
    fields = "__all__"