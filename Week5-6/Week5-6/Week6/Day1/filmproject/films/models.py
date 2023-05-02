from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField()
    
class Category(models.Model):
    name = models.CharField()
    
class Director(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    
class Film(models.Model):
    title = models.CharField()
    release_date = models.DateField(auto_now_add=True, blank=True)
    created_in_country = models.ForeignKey(Country, on_delete = models.SET_NULL, null = True, related_name='film_created') 
    available_in_countries = models.ManyToManyField(Country, related_name='film_available') 
    category = models.ManyToManyField(Category) 
    director = models.ManyToManyField(Director)