from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BookReview
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput()
            }
    