from signal import signal
from django.shortcuts import render, HttpResponse
from blog import signals

# Create your views here.
def home(request):
    # a = 10/0

    # Custom Signals 93
    signals.notification.send(sender=None, request=request, user=['SD','Goraya'])
    return HttpResponse('This is Home page')