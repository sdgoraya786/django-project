from django.db import models

# 1

STATE_CHOICE = (
    ('Azad Jammu and Kashmir','Azad Jammu and Kashmir'),
    ('Balochistan','Balochistan'),
    ('Gilgit-Baltistan','Gilgit-Baltistan'),
    ('Islamabad Capital Territory','Islamabad Capital Territory'),
    ('Khyber Pakhtunkhwa','Khyber Pakhtunkhwa'),
    ('Punjab','Punjab'),
    ('Sindh','Sindh'),
)

class Resume(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    state = models.CharField(choices=STATE_CHOICE, max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    moblie = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile-image')
    upload_cv = models.FileField(upload_to='cv')