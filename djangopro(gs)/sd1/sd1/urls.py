"""sd1 URL Configuration

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
from django.urls import path,include
from sd1 import views

from main_site import views as main_site
# from course import views as cv
# from fees import views as fv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    # path('lerandj/', cv.leran_django),
    # path('feesdj/', fv.fees_django),

    path('course/', include('course.urls')),

    # Template Inheritance 2nd method
    path('home/', main_site.home2, name='home'),
    path('about/', main_site.about, name='about'),
    path('fees/', include('fees.urls')),
]
