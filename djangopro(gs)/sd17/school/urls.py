from django.urls import path
from . import views

urlpatterns = [
    path('func/', views.myview, name='func'),
    path('cl/', views.MyView.as_view(), name='cl'),
    # path('cl/', views.MyView.as_view(name='MS'), name='cl'),
    path('subcl/', views.MyChildView.as_view(), name='cl'),
    #-----------------------------------------#
    #-----------------------------------------#
    path('homefunc/', views.homeview, name='homefunc'),
    path('homecl/', views.homeclassview.as_view(), name='homecl'),
    #-----------------------------------------#
    #-----------------------------------------#
    path('aboutfun/', views.aboutfun, name='aboutfun'),
    path('aboutcl/', views.adoutclassview.as_view(), name='aboutcl'),
    #-----------------------------------------#
    #-----------------------------------------#
    path('contactfun/', views.contactfun, name='contactfun'),
    path('contactcl/', views.contactclassview.as_view(), name='contactcl'),
    #-----------------------------------------#
    #-----------------------------------------#
    # path('newsfun/', views.newsfun, name='newsfun'),
    path('newsfun/', views.newsfun, {'template_name':'school/news.html'}, name='newsfun'),
    path('newsfun2/', views.newsfun, {'template_name':'school/news2.html'}, name='newsfun2'),

    # path('newscl/', views.newsclassview.as_view(), name='newscl'),
    path('newscl/', views.newsclassview.as_view(template_name='school/news.html'), name='newscl'),
    path('newscl2/', views.newsclassview.as_view(template_name='school/news2.html'), name='newscl'),
]