from django.shortcuts import render, HttpResponse
from .forms import ContactForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

# Create your views here.
# Generic Class Based View - Editing View: FormView - 114
class ContactFormView(FormView):
    template_name = 'school3/contact.html'
    form_class = ContactForm
    success_url = 'thanks/'
    initial = {'name':'SD Goraya'}

    # def form_valid(self, form):
    #     print(form.cleaned_data['name'])
    #     print(form.cleaned_data['email'])
    #     print(form.cleaned_data['message'])
    #     return super().form_valid(form)
    #     # return HttpResponse('Message Sent')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(self.get_form())
    #     return context
    
    # def get_context_data(self, **kwargs):
    #     context = super(ContactFormView, self).get_context_data(**kwargs)
    #     context["form_1"] = context["form"]
    #     return context
    


class ThanksView(TemplateView):
    template_name = "school3/thanks.html"
