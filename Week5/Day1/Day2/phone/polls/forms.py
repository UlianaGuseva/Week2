from django import forms
from .models import Person
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class NewPersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('phone_number', 'name')
        widgets = {
            'phone_number': PhoneNumberPrefixWidget(
            country_choices=[
                 ("IL", "Israel"),
            ],
        ),
    }
    def __init__(self, *args, **kwargs):
        super(NewPersonForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].required = False
        self.fields['name'].required = False
        
    