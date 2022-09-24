from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    # ----------------118,119------------------
    # path('', views.home, name='home'),
    # path('accounts/profile/', views.profile, name='profile'),

    # ----------------120,121------------------
    # method 1 for use Decorators in url not best
    # path('', views.homeTemplateView.as_view(), name='home'),
    # path('accounts/profile/', login_required(views.ProfileTemplateView.as_view()), name='profile'),
    # path('accounts/about/', staff_member_required(views.AboutTemplateView.as_view()), name='about'),
    # method 2 for use Decorators in class
    path('', views.homeTemplateView.as_view(), name='home'),
    path('accounts/profile/', views.ProfileTemplateView.as_view(), name='profile'),
    path('accounts/about/', views.AboutTemplateView.as_view(), name='about'),
]