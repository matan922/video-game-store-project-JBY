from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProfileManager(models.Manager):
    def get_or_create_profile(self, user):
        try:
            profile = self.get(user=user)
        except Profile.DoesNotExist:
            profile = self.create(user=user)
        return profile

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    objects = ProfileManager()

    def __init__(self, *args, **kwargs):
        super(Profile, self).__init__(*args, **kwargs)
        self.location = "Unknown"
        self.bio = "I'm a new user!"

    def __str__(self):
        return self.user.username

