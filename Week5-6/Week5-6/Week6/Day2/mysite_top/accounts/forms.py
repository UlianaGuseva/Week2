from django import forms
from .models import UserProfile, MyUser

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        widgets = {
            "user": forms.HiddenInput()
        }
        
class MyUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = '__all__'
        widgets = {'date_of_birth': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'})}