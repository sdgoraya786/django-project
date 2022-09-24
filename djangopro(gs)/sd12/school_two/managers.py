from django.db import models

# Custom Model Manager 103
# Modify The Initial QuerySet

class CustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('name')
