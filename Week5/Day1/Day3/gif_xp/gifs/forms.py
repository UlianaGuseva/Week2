from django import forms
from .models import Category

class Gif(forms.Form):
    name = forms.CharField(max_length=50)
    url = forms.URLField()
    uploader_name = forms.CharField(max_length=50)
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
    
    
class Category(forms.Form):
    name = forms.CharField(max_length=50)
    