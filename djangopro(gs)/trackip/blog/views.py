from turtle import title
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Post
from django.contrib.auth.models import Group
from .forms import SignUpForm, LoginForm, PostForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

from django.core.cache import cache

# Home
def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts':posts})

# About
def about(request):
    return render(request, 'blog/about.html')

# Contact
def contact(request):
    return render(request, 'blog/contact.html')

# Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        ip = request.session.get('ip', 0)
        ct = cache.get('count', version=user.pk)
        data = {
            'posts': posts,
            'username': user,
            'full_name': user.get_full_name(), # for get full name
            'groups': user.groups.all(),         # for get user group
            'ip': ip,
            'count': ct
        }
        return render(request, 'blog/dashboard.html', data)
    else:
        return redirect('login')

# Add New Post
def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PostForm(request.POST)
            if fm.is_valid():
                title = fm.cleaned_data['title']
                desc = fm.cleaned_data['desc']
                post = Post(title=title, desc=desc)
                post.save()
                messages.success(request, 'Post added successfully!')
                fm = PostForm()
        else:
            fm = PostForm()
        return render(request, 'blog/addpost.html', {'form':fm})
    else:
        return redirect('login')

# Update Post
def update_post(request,id):
    if request.user.is_authenticated:
        pi = Post.objects.get(pk=id)
        if request.method == 'POST':
            fm = PostForm(request.POST, instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Post Updated successfully!')
                return redirect('dashboard')
        else:
            fm = PostForm(instance=pi)
        return render(request, 'blog/updatepost.html', {'form':fm,'post':pi})
    else:
        return redirect('login')

## Delete Post Method 1
# def delete_post(request,id):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             pi = Post.objects.get(pk=id)
#             # pi.delete()
#             print(pi)
#             messages.success(request, 'Post Deleted successfully!')
#             return redirect('dashboard')
#         else:
#             return HttpResponse("<h3>401: Unauthorized Access!</h3>")
#     else:
#         return redirect('login')
## Delete Post Method 2
def delete_post(request,id):
    if request.user.is_authenticated & request.user.is_superuser == True:
        pi = Post.objects.get(pk=id)
        # pi.delete()
        print(pi)
        messages.success(request, 'Post Deleted successfully!')
        return redirect('dashboard')
    else:
        return HttpResponse("<h3>401: Unauthorized Access!</h3>") 

# Signup
def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = SignUpForm(request.POST)
            if fm.is_valid():
                user = fm.save()
                # Add Group
                # group = Group.objects.get(name="Author")
                # user.groups.add(group)
                messages.success(request, 'Congratulations! Your registration has been completed successfully. Now you can login!')
                return redirect('login')
        else:
            fm = SignUpForm()
        return render(request, 'blog/signup.html', {'form':fm})
    else:
        return redirect('dashboard')

# login [ *request.user* this is a bilten variable provided by django ]
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully!')
                    return redirect('dashboard')

        else:
            fm = LoginForm()
        return render(request, 'blog/login.html', {'form':fm})
    else:
        return redirect('dashboard')

# Logout
def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, 'blog/logout.html')
    else:
        return redirect('home')