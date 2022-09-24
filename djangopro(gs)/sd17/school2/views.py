from django.shortcuts import render
from django.views.generic.base import TemplateView

# Base Class-based View - TemplateView* 109

# class HomeTemplateView(TemplateView):
#     template_name='school2/home.html'


class HomeTemplateView(TemplateView):
    template_name='school2/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "SD Goraya"
        context["roll"] = 101
        # context = {
        #     'name': 'Sherazi Doctor',
        #     'roll': 102
        # }
        print(context)
        print(kwargs)
        return context
    