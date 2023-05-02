from django.db import models
from django.contrib.auth.models import User
# from polls.models import Post
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.URLField(null=True, blank=True)
    def __str__(self):
        return f'{self.user.username}'
