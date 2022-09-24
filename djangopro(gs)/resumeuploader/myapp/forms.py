from django import forms
from .models import Resume

# 8
GENDER_CHOICES = [
    ('Male','Male'),
    ('Female','Female')
]
JOB_CITY_CHOICES = [
    ('Lahore','Lahore'),
    ('Karachi','Karachi'),
    ('Pasror','Pasror'),
    ('Multan','Multan'),
    ('Quita','Quita'),
    ('Islamabad','Islamabad')
]

# 2
class ResumeForm(forms.ModelForm):

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Job Locations', choices=JOB_CITY_CHOICES, widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Resume
        fields = '__all__'
        labels = {
            'name':'Full Name', 'dob':'Date of Birth', 
            'pin':'Pin Code', 'moblie':'Mobile No.', 
            'profile_image':'Profile Image', 'upload_cv':'Upload CV'
        }
        # 7
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'locality': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.Select(attrs={'class':'form-select'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'pin': forms.NumberInput(attrs={'class':'form-control'}),
            'moblie': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }