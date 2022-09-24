from ntpath import join
from django.db import models
from django.contrib.auth.models import User

# Many to Many Relationship 106
class Song(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=100)
    song_duration = models.IntegerField()

    def written_by(self):
        return ", ".join([str(p) for p in self.user.all()])