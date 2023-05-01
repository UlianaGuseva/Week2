from django.shortcuts import render, redirect
from .models import Person
from .forms import NewPersonForm


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


def find_person(request):
    if request.method == 'POST':
        person_filled_form = NewPersonForm(request.POST)
        if person_filled_form.is_valid():
            name = person_filled_form.cleaned_data['name']
            phone_number = person_filled_form.cleaned_data['phone_number']
            
            if name:
                return redirect('by_data', name)
            else: 
                return redirect('by_data', phone_number)

    
    form = NewPersonForm()   
    context = {'form' : form}
    
    return render(request, 'form_newperson.html', context)

