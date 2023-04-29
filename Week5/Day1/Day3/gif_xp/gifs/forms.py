from django import forms
from .models import Gif, Category

class GifForm(forms.ModelForm):
    class Meta:
        model = Gif
        fields = ('name', 'url', 'uploader_name')
        exclude = ('likes',)
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
    
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

