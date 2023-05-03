from django import forms
from .models import Rental, Customer, Vehicle, Comment

class NewRentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = '__all__'
        widgets = {
            'rental_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}), 
            'return_date': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}
            )}
        
class NewCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
       
class NewVehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
        widgets = {
            'date_created': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)', 'class': 'form-control'}),
            }
        
class FindVehicle(forms.Form):
    id_v = forms.IntegerField()
    id_r = forms.IntegerField()
    id_c = forms.IntegerField()    
     
    def __init__(self, *args, **kwargs):
        super(FindVehicle, self).__init__(*args, **kwargs)
        self.fields['id_v'].required = False
        self.fields['id_r'].required = False
        self.fields['id_c'].required = False
        


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {'vehicle': forms.HiddenInput(),
                   'author': forms.HiddenInput(),
                   'content': forms.Textarea()}
