from django.db import models
from django.contrib.auth.models import User

# Many to One Relationship 105
class Post(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.PROTECT) # when we delete all post of user then we delete that user 
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # if we delete user then set null in that post user
    post_title = models.CharField(max_length=70)
    post_cat = models.CharField(max_length=70)
    post_publish_date = models.DateField()

    def __str__(self):
        return self.post_title