from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    admin = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='admin')
    
    def __str__(self):
        return str(self.name)
    
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='department')
    project = models.ManyToManyField('Project')
    def __str__(self):
        return str(self.name)
    
class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    due_date =models.DateField()
    completed = models.BooleanField(default=False)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name)
    
class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date =models.DateField()
    
    def __str__(self):
        return str(self.name)

