from django.db import models
from datetime import datetime

# Create your models here.
class Gif(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    uploader_name = models.CharField(max_length=50)
    created_at = datetime.now() #models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.name}"
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    gifs = models.ManyToManyField('Gif', related_name='categories')
    
    def __str__(self):
        return f"{self.name}"