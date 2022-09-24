from .models import Page
from django.db.models.signals import post_delete
from django.dispatch import receiver

# One to One Relationship - Reverse Relation 104

@receiver(post_delete, sender=Page)
def delete_releated_user(sender, instance, **kwargs):
    # print('Post delete')
    # print(instance.user)
    instance.user.delete()