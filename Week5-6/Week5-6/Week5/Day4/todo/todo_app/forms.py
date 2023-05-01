from django import forms
from .models import Todo, Category

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ('date_completion', 'has_been_done')
        widgets = {
            'deadline_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )}
    