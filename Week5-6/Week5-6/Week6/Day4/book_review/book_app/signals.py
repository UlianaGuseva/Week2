from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg
from .models import Book, BookReview

@receiver(post_save, sender=BookReview)
def create_book_review(sender, instance, created, **kwargs):
    if created:
        book = Book.objects.get(id=instance.book.id)
        book.number_reviews += 1
        q = BookReview.objects.aggregate(Avg("rating"))
        book.book_rating = q['rating__avg']
        book.save()
        print('saved')
    
    
