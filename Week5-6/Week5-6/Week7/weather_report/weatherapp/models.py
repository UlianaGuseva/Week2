from django.db import models
from django.contrib.auth.models import User

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
    forecaster = models.ForeignKey('Forecaster', on_delete=models.SET_NULL, null=True)

class Forecaster(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='forecaster')
   
   def __str__(self):
      return str(self.user)