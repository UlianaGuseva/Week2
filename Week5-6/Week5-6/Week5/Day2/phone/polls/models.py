
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(unique=True)
    phone_number = PhoneNumberField(blank=True)
    address = models.CharField()
    
    def __str__(self):
        return f'{self.name} | {self.phone_number} | {self.address} | {self.email}'
    
    
