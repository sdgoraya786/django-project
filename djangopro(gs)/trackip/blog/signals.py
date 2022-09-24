from ensurepip import version
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver

from django.core.cache import cache

@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    # Track Clint IP 91
    ip = request.META.get('REMOTE_ADDR')
    request.session['ip'] = ip

    # User login count 92
    ct = cache.get('count', 0, version=user.pk)  # (version=user.pk) for every user have seprate cache
    newcount = ct + 1
    cache.set('count', newcount, 60*60*24, version=user.pk)