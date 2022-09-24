"""sdgoraya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sdgoraya import views

# Upload a File with FileField(2)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about-us/', views.aboutUs, name='about-us'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<slug:courseid>', views.blogDetails),
    path('contact/', views.contact),
    path('courses/', views.courses, name='courses'),
    path('newsdetails/<slug>', views.newsDetails),

    path('user-form/', views.userForm),
    path('submitForm/', views.submitForm, name='submitForm'),

    path('dj-forms/', views.djForms, name='djForms'),

    path('calculator/', views.calculator, name='calculator'),
    path('evenodd/', views.evenOdd),
    path('marksheet/', views.marksheet),
]

# Upload a File with FileField(3)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)