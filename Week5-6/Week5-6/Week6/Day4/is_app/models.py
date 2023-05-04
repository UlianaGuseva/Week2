from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    image = models.URLField()
    title = models.CharField()
    description = models.CharField()
    user_uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_upoader')
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    number_images = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return f'{self.user.username}'
    