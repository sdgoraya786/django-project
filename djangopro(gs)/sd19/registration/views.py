from django.shortcuts import render
# 119
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# 120
from django.views.generic import TemplateView
# 121
from django.utils.decorators import method_decorator
# Create your views here.

"""**************************************************************
    use Authentication Views with Function Based View 118
    and login required and staff member required Decorators 119
**************************************************************"""
# def home(request):
#     return render(request, 'registration/home.html')

# @login_required
# def profile(request):
#     return render(request, 'registration/profile.html')

# @staff_member_required
# def profile(request):
#     return render(request, 'registration/about.html')



"""**************************************************************
    use Authentication Views with Class Based View 120
    and login required and staff member required Decorators 121
**************************************************************"""
## Method 1
# class homeTemplateView(TemplateView):
#     template_name = "registration/home.html"
# class ProfileTemplateView(TemplateView):
#     template_name = "registration/profile.html"
# class AboutTemplateView(TemplateView):
#     template_name = "registration/about.html"

## Method 2
# class homeTemplateView(TemplateView):
#     template_name = "registration/home.html"
# class ProfileTemplateView(TemplateView):
#     template_name = "registration/profile.html"

#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)
    
# class AboutTemplateView(TemplateView):
#     template_name = "registration/about.html"

#     @method_decorator(staff_member_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(request, *args, **kwargs)

## Method 2
class homeTemplateView(TemplateView):
    template_name = "registration/home.html"
@method_decorator(login_required, name='dispatch')
class ProfileTemplateView(TemplateView):
    template_name = "registration/profile.html"
    
class AboutTemplateView(TemplateView):
    template_name = "registration/about.html"