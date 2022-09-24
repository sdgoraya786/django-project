from django.shortcuts import render
from .models import Page, Post, Song, User

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')

def show_user_data(request):
    ud1 = User.objects.all()

    # ud2 = User.objects.filter(page__page_cat='Medical')
    ud2 = User.objects.filter(page__page_cat__icontains='medical')
    ud3 = User.objects.filter(post__post_publish_date='2022-06-26')
    ud4 = User.objects.filter(song__song_duration=6)

    data = {
        'data1': ud1,
        'data2': ud2,
        'data3': ud3,
        'data4': ud4,
    }
    return render(request, 'myapp/user.html', data)

def show_page_data(request):
    pd1 = Page.objects.all()
    pd2 = Page.objects.filter(page_cat__icontains='medical')
    pd3 = Page.objects.filter(user__is_staff=1)

    data = {
        'data1': pd1,
        'data2': pd2,
        'data3': pd3,
    }
    return render(request, 'myapp/page.html', data)

def show_post_data(request):
    pd1 = Post.objects.all()
    pd2 = Post.objects.filter(post_publish_date='2022-06-26')
    pd3 = Post.objects.filter(user__username='maha')

    data = {
        'data1': pd1,
        'data2': pd2,
        'data3': pd3,
    }
    return render(request, 'myapp/post.html', data)

def show_song_data(request):
    sd1 = Song.objects.all()
    sd2 = Song.objects.filter(song_duration=6)
    sd3 = Song.objects.filter(user__username='maha')
    data = {
        'data1': sd1,
        'data2': sd2,
        'data3': sd3,
    }
    return render(request, 'myapp/song.html', data)
