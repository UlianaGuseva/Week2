from django.db import models

TYPE_CHOICES = (
   ('sunny', 'Sunny'),
   ('cloudy', 'Cloudy'),
   ('windy', 'Windy'),
   ('rainy', 'Rainy'),
   ('stormy', 'Stormy')
)
# Create your models here.
class Report(models.Model):
    location = models.CharField(max_length=50)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, blank=True, null=True)