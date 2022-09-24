from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User

from django.dispatch import receiver, Signal

from django.db.models.signals import pre_init, post_init, pre_save, post_save, pre_delete, post_delete, pre_migrate, post_migrate

from django.core.signals import request_started, request_finished, got_request_exception

from django.db.backends.signals import connection_created

# Signals 90
# Singnal Connect to our Receiver Function (Connnecting/Registering Receiver Function) (ii.ii)
# Decorator @receiver
@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):    # Receiver Function (i)
    print('-----------------------------------------') 
    print('Logged in signals - Run Intro....')
    print('Sender:', sender)
    print('Request:', request)
    print('User:', user)
    print('User Password:', user.password)
    print(f'kwargs: {kwargs}')
    print('-----------------------------------------')

# Singnal Connect to our Receiver Function (Connnecting/Registering Receiver Function) (ii.i)
# Manual Connect Route - Signal.connect () Method
# user_logged_in.connect(login_success, sender=User)


@receiver(user_logged_out, sender=User)
def logout_success(sender, request, user, **kwargs):    # Receiver Function (i)
    print('-----------------------------------------') 
    print('Logged-out signals - Run Outro....')
    print('Sender:', sender)
    print('Request:', request)
    print('User:', user)
    print(f'kwargs: {kwargs}')
    print('-----------------------------------------')

@receiver(user_login_failed)
def logout_success(sender, credentials, request, **kwargs):    # Receiver Function (i)
    print('-----------------------------------------') 
    print('Logged-in Failed signals....')
    print('Sender:', sender)
    print('Credentials:', credentials)
    print('Request:', request)
    print(f'kwargs: {kwargs}')
    print('-----------------------------------------')

# Model Signals
@receiver(pre_save, sender=User)
def at_beginning_save(sender, instance, **kwargs):    # Receiver Function
    print('-----------------------------------------') 
    print('Pre Save signals....')
    print('Sender:', sender)
    print('Instance:', instance)
    print(f'kwargs: {kwargs}')
    print('-----------------------------------------')

@receiver(post_save, sender=User)
def at_ending_save(sender, instance, created, **kwargs):    # Receiver Function
    if created:
        print('-----------------------------------------') 
        print('Post Save signals....')
        print('New Record')
        print('Sender:', sender)
        print('Instance:', instance)
        print('Created:', created)
        print(f'kwargs: {kwargs}')
        print('-----------------------------------------')
    else:
        print('-----------------------------------------') 
        print('Post Save signals....')
        print('Update Record')
        print('Sender:', sender)
        print('Instance:', instance)
        print('Created:', created)
        print(f'kwargs: {kwargs}')
        print('-----------------------------------------')

@receiver(pre_delete, sender=User)
def at_beginning_delete(sender, instance, **kwargs):    # Receiver Function
    print('-----------------------------------------') 
    print('Pre Delete signals....')
    print('Sender:', sender)
    print('Instance:', instance)
    print(f'kwargs: {kwargs}')
    print('-----------------------------------------')

@receiver(post_delete, sender=User)
def at_ending_delete(sender, instance, **kwargs):    # Receiver Function
    print('-----------------------------------------') 
    print('Post Delete signals....')
    print('Sender:', sender)
    print('Instance:', instance)
    print(f'kwargs: {kwargs}')
    print('-----------------------------------------')

@receiver(pre_init, sender=User)
def at_beginning_delete(sender, *args, **kwargs):    # Receiver Function
    print('-----------------------------------------') 
    print('Pre init signals....')
    print('Sender:', sender)
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
    print('-----------------------------------------')

@receiver(post_init, sender=User)
def at_ending_delete(sender, *args, **kwargs):    # Receiver Function
    print('-----------------------------------------') 
    print('Post init signals....')
    print('Sender:', sender)
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')
    print('-----------------------------------------')

# Request-Response Signals
@receiver(request_started)
def at_beginning_request(sender, environ, **kwargs):    # Receiver Function
    print('-----------------------------------------') 
    print('Request Beginning signals....')
    print('Sender:', sender)
    print('Environ:', environ)
    print(f'kwargs: {kwargs}')
    print('-----------------------------------------')

@receiver(request_finished)
def at_ending_request(sender, **kwargs):    # Receiver Function
    print('-----------------------------------------') 
    print('Request Ending signals....')
    print('Sender:', sender)
    print(f'kwargs: {kwargs}')
    print('-----------------------------------------')

@receiver(got_request_exception)
def at_request_exception(sender, request, **kwargs):    # Receiver Function
    print('-----------------------------------------') 
    print('Request Exception signals....')
    print('Sender:', sender)
    print('Request:', request)
    print(f'kwargs: {kwargs}')
    print('-----------------------------------------')


# Management Signals
@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):    # Receiver Function
    print('-----------------------------------------') 
    print('Before App Install signals....')
    print('Sender:', sender)
    print('App Config:', app_config)
    print('Verbosity:', verbosity)
    print('Interactive:', interactive)
    print('Using:', using)
    print('Plan:', plan)
    print('Apps:', apps)
    print(f'kwargs: {kwargs}')
    print('-----------------------------------------')

@receiver(post_migrate)
def at_end_migrate_flush(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):    # Receiver Function
    print('-----------------------------------------') 
    print('After App Install signals....')
    print('Sender:', sender)
    print('App Config:', app_config)
    print('Verbosity:', verbosity)
    print('Interactive:', interactive)
    print('Using:', using)
    print('Plan:', plan)
    print('Apps:', apps)
    print(f'kwargs: {kwargs}')
    print('-----------------------------------------')


# Database Wrappers
@receiver(connection_created)
def conn_db(sender, connection, **kwargs):    # Receiver Function
    print('-----------------------------------------') 
    print('Initial Connection to database....')
    print('Sender:', sender)
    print('Connection:', connection)
    print(f'kwargs: {kwargs}')
    print('-----------------------------------------')


"""******************************
       Custom Signals 93
******************************"""
# notification = Signal(providing_args=["request","user"])
notification = Signal()

@receiver(notification)
def show_notification(sender, **kwargs):    # Receiver Function
    print('-----------------------------------------') 
    print('Notification....')
    print('Sender:', sender)
    print(f'kwargs: {kwargs}')
    print('-----------------------------------------')