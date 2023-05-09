from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile, Image

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    print(f'Creating a profile for user {instance}')
    
@receiver(post_save, sender=Image)
def create_image(sender, instance, created, **kwargs):
    print('create new image')
    if created:
        current_user = instance.user_uploader.profile
        current_user.number_images += 1 
        current_user.save()
        print(f'Created post of {current_user.number_images}')
    
    