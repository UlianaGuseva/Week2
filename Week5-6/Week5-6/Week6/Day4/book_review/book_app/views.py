from django.shortcuts import render
from django.views.generic import DetailView, CreateView, ListView
from .forms import RegisterForm, ReviewForm
from django.urls import reverse_lazy
from .models import Book, BookReview
# Create your views here.
class SignUpView(CreateView):
    
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    
class AllBooks(ListView):
    template_name = "all_books.html"
    model = Book
    context_object_name = 'books'
    
def book_details(request, id):
    book = Book.objects.get(id=id)
    reviews = BookReview.objects.filter(book=id)
    context = {'book': book, 'reviews': reviews}
    return render(request, 'book_detail.html', context)  
    
class AddReview(CreateView):
    login_url = reverse_lazy('login')
    template_name = 'add_review.html'
    form_class = ReviewForm
    model = BookReview
    success_url = reverse_lazy('all_books')
    def get_initial(self):
        user = self.request.user
        initial_data = {'user': user}
        return initial_data
    
class ReviewDetais(DetailView):
    template_name = 'review_details.html'
    context_object_name = 'info'
    model = BookReview