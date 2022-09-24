from django import forms
from . import models as mymodel
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation

class CustomerRegistration(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class':'form-control'}),
        # help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class':'form-control'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ['username','password1','password2']
        widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}


class CustomerLogin(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True,'class':'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",'class':'form-control'}),
    )


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True, 'class': 'form-control'}
        ),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class': 'form-control'}),
    )

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email Address"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", 'class': 'form-control'}),
    )

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class': 'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("Confirm password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class': 'form-control'}),
    )


class CustomerAddAddressForm(forms.ModelForm):
    class Meta:
        model = mymodel.CustomerAddress
        fields = ['name','state','city','address','Zipcode']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.Select(attrs={'class':'form-select'}),
            'city': forms.Select(attrs={'class':'form-select'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'Zipcode': forms.TextInput(attrs={'class':'form-control'}),
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = mymodel.City.objects.none()

        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['city'].queryset = mymodel.City.objects.filter(
                    state_id=state_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk and self.instance.state:
            self.fields['city'].queryset = self.instance.state.city_set

