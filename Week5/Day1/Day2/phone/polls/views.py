from django.shortcuts import render
from .models import Person


# Create your views here.
def search(model, value):
    result = None
    try:
        model_instance = model.objects.get(name=value)
        result = model_instance
    except model.DoesNotExist:
        pass
    try:
        model_instance = model.objects.get(phone_number=value)
        result = model_instance
    except model.DoesNotExist:
        pass
    return result

def get_by_data(request, info):
    context = {}
    info = search(Person, info)
    
    if info is not None:
        context = {'data': info}     
    
    return  render(request, 'index_byphonenum.html', context)

# def get_by_name(request, name):
#     context = {'data': Person.objects.get(name=name)}
#     return  render(request, 'index_byname.html', context)

