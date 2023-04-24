from django.shortcuts import render
from .models import Animal, Family

# def read_data(location, key):
#     with open(location, 'r') as file:
#         data = json.load(file)
#     sub_data = data[key]
#     return sub_data

# Create your views here.


def families(request, id):
    
    context = {'names': Animal.objects.filter(family_id=id)}
    return  render(request, 'index_families.html', context)
    
def animals(request, id):
    context = {'data': Animal.objects.get(id=id)}
    return  render(request, 'index_animals.html', context)

def all_animals(request):
    context = {'data': Animal.objects.all,
               'families_names': Family.objects.all}
    return  render(request, 'index_all_animals.html', context)

            
