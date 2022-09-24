from tokenize import group
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, Group
# 74,77,78
from .forms import SingUpForm, EditUserProfileForm, EditAdminProfileForm
# 74,75,76,77
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
# 75,76
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Change Password with Old Password and without Old Password 76




# Create your views here.

"""****************************************************************************
    Create Registration Form using UserCreationForm by default fields (p1)
    sigup view function
****************************************************************************"""

# def sign_up(request):
#     if request.method == 'POST':
#         fm = UserCreationForm(request.POST)
#         if fm.is_valid():
#             fm.save()
#     else:
#         fm = UserCreationForm()
#     return render(request, 'enroll/singup.html', {'form':fm})


##  Inheriting UserCreationForm for more fields 74 (p2) ##
def sign_up(request):
    if request.method == 'POST':
        fm = SingUpForm(request.POST)
        if fm.is_valid():
            user = fm.save()
            messages.success(request, 'Account create successfully.')

            ## Join Group while Registration 79 ##
            group = Group.objects.get(name="Editor")
            user.groups.add(group)

    else:
        fm = SingUpForm()
    return render(request, 'enroll/singup.html', {'form':fm})


"""****************************************************************************
    Create Login Form using AuthenticationForm and Profile Page and Logout 75
    login view function
****************************************************************************"""
def user_login(request):
    ## for check user login or not [is_authenticated return true] if user already login then redirect to profile page ##
    if not request.user.is_authenticated:
        if request.method == 'POST':
            ## for show login form ##
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                ## for authenticate(match) username and password ##
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully.')
                    return redirect('profile')
                
        else:
            ## for show login form ##
            fm = AuthenticationForm()
        return render(request, 'enroll/login.html', {'form':fm})
    else:
        return redirect('profile')

## for profile page 75 ##
def user_logout(request):
    logout(request)
    messages.success(request, 'Logout successfully.')
    return redirect('login')

## for profile page 75
def user_profile(request):
    ## for check user login or not [is_authenticated return true] if user not login then redirect to login page ##
    if request.user.is_authenticated:
        users = None
        if request.user.is_superuser == True:
            ## for get all users for admin 78
            users = User.objects.all()
        return render(request, 'enroll/profile.html', {'users':users})
    else:
        return redirect('login')


"""**************************************************************************** 
    Profile using UserChangeForm 77 edit user profile
****************************************************************************"""

def user_profileedit(request):
    ## for check user login or not [is_authenticated return true] if user not login then redirect to login page ##
    if request.user.is_authenticated:
        # fm = UserChangeForm(instance=request.user)
        if request.method == "POST":
            """ ## User Profile and Admin Profile 78 ## """
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST, instance=request.user)
            else:
                fm = EditUserProfileForm(request.POST, instance=request.user)

            if fm.is_valid():
                fm.save()
                messages.success(request, 'Profile Update successfully.')
                return redirect('profile')
        else:
            """ ## User Profile and Admin Profile 78 ## """
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(instance=request.user)
            else:
                fm = EditUserProfileForm(instance=request.user)
        return render(request, 'enroll/editprofile.html', {'name':request.user, 'form':fm})
    else:
        return redirect('login')

""" ## for admin user detail page 78 ## """
def user_detail(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser == True:
            pi = User.objects.get(pk=id)
            fm = EditAdminProfileForm(instance=pi)
            return render(request, 'enroll/userdetail.html', {'username':pi, 'form':fm})
        else:
            return HttpResponse("<h3>401: Unauthorized Request</h3>")
    else:
        return redirect('login')

"""****************************************************************************
    Change Password with Old Password and without Old Password 76
****************************************************************************"""

## Change Password with Old Password 76 ##
def user_ChangePassword(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            ## for show Change Password form ##
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                # if you whant to update user sessioon
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password Change successfully.')
                return redirect('profile')
        else:
            ## for show Change Password form ##
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'enroll/changepassword.html', {'form':fm})
    else:
        return redirect('login')

## Change Password without Old Password 76 ##
def user_ChangePassword2(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            ## for show Change Password form ##
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                # if you whant to update user sessioon
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password Change successfully.')
                return redirect('profile')
        else:
            ## for show Change Password form ##
            fm = SetPasswordForm(user=request.user)
        return render(request, 'enroll/changepassword2.html', {'form':fm})
    else:
        return redirect('login')