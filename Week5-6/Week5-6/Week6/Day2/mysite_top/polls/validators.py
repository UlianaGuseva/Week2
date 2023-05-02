from django.core.exceptions import ValidationError
from datetime import date

def date_validator(date_submit: date):
    today = date.today()
    if date_submit > today:
        raise ValidationError('can not be from future')
    
