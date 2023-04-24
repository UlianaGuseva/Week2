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
    
    # one to one relationship - Profile (parent name, country origin, languages)

class Profile(models.Model):
    # one to one relationship - Profile (parent name, country origin, languages)
    person = models.OneToOneField('Person', on_delete=models.CASCADE)
    counrty_origin = models.CharField(max_length=50)
    # many to many relationship - Profile (parent name, country origin, languages)
    languages = models.ManyToManyField('Language')
    def __str__(self):
        return f"{self.counrty_origin}"
    
class Language(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return f"{self.name}"