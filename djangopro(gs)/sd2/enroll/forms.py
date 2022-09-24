from django.core import validators  #61
from django import forms

class StudentRegistration(forms.Form):
    first_name = forms.CharField(initial='Shahzad', help_text='Name must be a string')

"""////// Loop Form Fields 50 ///////"""
class StudentRegistration2(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.IntegerField()

"""/////// Form Hidden Fields 50 ///////"""
class StudentRegistration3(forms.Form):
    key = forms.CharField(widget=forms.HiddenInput)
    name = forms.CharField()

"""/////// Form Field Argument 51 ///////"""
class StudentRegistration4(forms.Form):
    name = forms.CharField(label='Your Name', label_suffix=' ', initial='SD Goraya', required=False, disabled=True, help_text='Name must be string')

"""/////// Form Widgets 52 ///////"""
class StudentRegistration5(forms.Form):
    key = forms.CharField(widget=forms.HiddenInput)
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'somecss1','id':'UniqueId'}))
    password = forms.CharField(widget=forms.PasswordInput)
    message = forms.CharField(widget=forms.Textarea)
    check = forms.CharField(widget=forms.CheckboxInput)
    image = forms.CharField(widget=forms.FileInput)
    
"""/////// Form using Method POST and CSRF Token 55 ///////"""
class StudentRegistration6(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()


""" ///// Get Form Data and Validate Data 56 ////// """
class PostFormData(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()

""" ///// Form Fields 58 ////// """
class FormField(forms.Form):
    name = forms.CharField(error_messages={'required':'Enter Your Name'})  # strip=True remove whitespace in input, empty_value='SD GORAYA'
    email = forms.EmailField(error_messages={'required':'Enter Your Email','invalid':'Please Enter a valid email address'})
    roll = forms.IntegerField(min_value=1)
    price = forms.DecimalField(min_value=1, max_value=40,max_digits=5, decimal_places=2)
    rate = forms.FloatField(min_value=1, max_value=40,error_messages={'min_value':'Value is grater then or equal 1'})
    comment = forms.SlugField()
    website = forms.URLField()
    password = forms.CharField(min_length=8, widget=forms.PasswordInput)
    description = forms.CharField(min_length=20, widget=forms.Textarea(attrs={'class':'somecss1'}))
    feedback = forms.CharField(min_length=10, widget=forms.TextInput(attrs={'class':'somecss2'}))
    notes = forms.CharField(min_length=10, widget=forms.Textarea(attrs={'rows':3, 'cols':50}))
    agree = forms.BooleanField(label='I Agree Terms and Conditions', label_suffix='', error_messages={'required':'Please Select Ckeckbox'})


""" ///// Custom Cleaning and Validating Specific Form Field 59 ////// """
class CleanValidation(forms.Form):
    # name = forms.RegexField(regex='/^[A-Za-z]+$/',error_messages={'required':'Please Enter Your Name','invalid':'Please Enter Only Charactors'})
    uname = forms.CharField(label='Name')
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    # Custom validations
    def clean_name(self):
        valname = self.cleaned_data['uname']
        if len(valname) < 4:
            raise forms.ValidationError('Enter more then or equal 4 charactors.')
        if valname != '/^[A-Za-z]+$/':
            raise forms.ValidationError('Please Enter Only Charactors')
        return valname

""" ///// Custom Validating Complete Django Form at Once 60 ////// """
class ValidationFullForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    # Custom Validating [this not work properly]
    # def clean(self):
    #     cleaned_data = super().clean()
        # valpassword = cleaned_data['password']
        # valemail = cleaned_data['email']
        # if len(valpassword) < 6:
        #     raise forms.ValidationError('Enter more then or equal 6 charactors.')
        # if valname == '/^[A-Za-z]+$/':
        #     raise forms.ValidationError('Please Enter Only Charactors')
        # if len(valemail) < 10:
        #     raise forms.ValidationError('Email must be grater then or equal 6')
        
    # def clean(self):
    #     super().clean()
    #     name = self.cleaned_data["name"]
    #     password = self.cleaned_data["password"]

    #     if len(name) < 4:
    #         namemsg1 = 'Name must be grater then or equal 4'
    #         self.add_error('name', namemsg1)

    #     if len(password) < 6:
    #         msg2 = 'Pass must be grater then or equal 6'
    #         self.add_error('password', msg2)
            
""" ///// Built in Validators 61 ////// """
class BuiltinValidators(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10)])
    email = forms.EmailField()


""" ///// Custom Form Validators 61 ////// """
def statrs_with_s(value):
    if value[0] != 's':
        raise forms.ValidationError('Name shoul starts with s')
        
class CustomValidators(forms.Form):
    name = forms.CharField(validators=[statrs_with_s])
    email = forms.EmailField()

""" ///// Match Password and Re Enter Password 62 ////// """
class MatchPasswordRePassword(forms.Form):
    password22 = forms.CharField(label='Password', widget=forms.PasswordInput)
    again_password22 = forms.CharField(label='Password(again)', widget=forms.PasswordInput)

    # def clean(self):
    #     cleaned_data = super().clean()
    #     pswd = self.cleaned_data['password22']
    #     rpswd = self.cleaned_data['again_password22']
    #     if pswd != rpswd:
    #         raise forms.ValidationError('Password not Match')

    def clean(self):
        if(self.cleaned_data['password22'] != self.cleaned_data['again_password22']):
            raise forms.ValidationError('Password not Match')
            return self.cleaned_data


""" ///// Styling Django Form Errors and Field Error 63 ////// """
class StyleFieldErrors(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Name'}), error_messages={'required':'Enter Your Name'})
    email = forms.EmailField(min_length=5, error_messages={'required':'Enter Your Email'})
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required':'Enter Your Password'})



""" ///// Save Update and Delete Django Form(API) Data to/from Database 64 ////// """
class CRUD_DjangoForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Name'}), error_messages={'required':'Enter Your Name'})
    email = forms.EmailField(error_messages={'required':'Enter Your Email'})
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required':'Enter Your Password'})
    comment = forms.CharField(error_messages={'required':'Enter Your Comment'})