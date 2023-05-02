from django import forms
from .models import Post
from django.core.exceptions import ValidationError
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'author': forms.HiddenInput(),
            'date_created': forms.DateInput(attrs={'type': 'date'})
            }
        
    def clean_title(self):
        title = self.cleaned_data['title']
        if title.startswith('A'):
            raise ValidationError('The title should not start with letter A')
        return title
    
    def clean(self):
        cleaned_data = super().clean()
        author = cleaned_data['author']
        title = cleaned_data['title']
        
        if author.user.username.lower() == 'uliana':
            if title.lower() == 'test':
                raise ValidationError("The user Uliana can not write the 'test' post")
        