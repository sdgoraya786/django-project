from django.db import models
from django.contrib.auth.models import User

# One to One Relationship with Model Inheritance 104
class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='+')
    
    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField()

    def __str__(self) :
        return self.page_name

class Like(Page):
    page = models.OneToOneField(Page, on_delete=models.CASCADE, parent_link=True, primary_key=True, related_name='+')
    likes = models.IntegerField()