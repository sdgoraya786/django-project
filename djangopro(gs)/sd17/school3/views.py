from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView

# Base Class-based View - RedirectView* 110
class SDRedirectView(RedirectView):
    url = 'https://sdgoraya.pythonanywhere.com'

class SDGRedirectView(RedirectView):
    pattern_name = 'mindex'
    permanent = True
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        print(kwargs)
        # kwargs['pk'] = 23
        return super().get_redirect_url(*args, **kwargs)

# class HomeTemplateView(TemplateView):
#     template_name='school3/home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["name"] = ""
#         # context["roll"] = 101
#         print(context)
#         print(kwargs)
#         return context