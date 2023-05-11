from django.contrib import admin
from book_app.models import Book, BookReview

# Register your models here.
admin.site.register(Book)
admin.site.register(BookReview)
