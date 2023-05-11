from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50) 
    author = models.CharField(max_length=50) 
    published_date = models.DateField() 
    description = models.TextField() 
    page_count = models.IntegerField(default=0) 
    categories = models.CharField(max_length=50)
    thumbnail_url = models.URLField() 
    number_reviews = models.IntegerField(default=0)
    reviews = models.ForeignKey('BookReview', on_delete=models.CASCADE, null=True, blank=True, related_name='reviews')
    book_rating = models.FloatField(default=0)
    
    def __str__(self):
        return str(self.title)
    
class BookReview(models.Model):
    name = models.CharField(max_length=100, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    rating = models.IntegerField(default=0) 
    review_text = models.TextField()
    
    def __str__(self):
        return str(self.name)
    
