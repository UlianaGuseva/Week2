from django.db import models
from accounts.models import UserProfile



# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone_number = models.CharField(blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    # comment = models.TextField(null=True, blank=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
class Vehicle_Type(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Vehicle_Size(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Vehicle(models.Model):
    vehicle_type =  models.ForeignKey(Vehicle_Type, on_delete = models.SET_NULL, null = True, related_name='type')
    date_created = models.DateField()
    real_cost =  models.IntegerField()
    size =   models.ForeignKey(Vehicle_Size, on_delete = models.SET_NULL, null = True, related_name='size')

    def __str__(self):
        return f'{self.id} {self.size} {self.vehicle_type} '

class Rental_Rate(models.Model):
    daily_rate = models.FloatField()
    vehicle_type = models.ForeignKey(Vehicle_Type, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(Vehicle_Size, on_delete=models.CASCADE)

class Rental(models.Model):
    rental_date = models.DateField()
    return_date = models.DateField(blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    vehicle =  models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, blank=True)
    


class Comment(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self) -> str:
        return f"{self.vehicle}| {self.created_at} | {self.short_content()}"
    
    def short_content(self):
        return self.content[:15]
    
