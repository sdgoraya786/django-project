from django.db import models
from django.contrib.auth.models import User

# One to One Relationship
class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)  # if user post exist then user cannot delete user
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, limit_choices_to={'is_staff':True})
    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField()

    def __str__(self):
        return self.page_name

# One to Many Relationship
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.PROTECT) # when we delete all post of user then we delete that user 
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # if we delete user then set null in that post user
    post_title = models.CharField(max_length=70)
    post_cat = models.CharField(max_length=70)
    post_publish_date = models.DateField()

    def __str__(self):
        return self.post_title

# Many to Many Relationship
class Song(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=100)
    song_duration = models.IntegerField()

    def written_by(self):
        return ", ".join([str(p) for p in self.user.all()])