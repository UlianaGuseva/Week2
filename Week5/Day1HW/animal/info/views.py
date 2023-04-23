from django.shortcuts import render
from django.http import HttpResponse
import json
from django.template import loader

# filename = 'data.json'
# data = {
#     "animals": [
#         {
#             "id" :1,
#             "name": "Dog",
#             "legs": 4,
#             "weight": 5.67,
#             "height":4.2,
#             "speed": 34,
#             "family": 2
#         },
#         {
#             "id": 2,
#             "name": "Domestic Cat",
#             "legs": 2,
#             "weight": 5.67,
#             "height":4.2,
#             "speed": 34,
#             "family": 1
#         },
#         {
#             "id": 3,
#             "name": "Panther",
#             "legs": 2,
#             "weight": 5.67,
#             "height":4.2,
#             "speed": 34,
#             "family": 1 
#         },
#         {
#             "id": 4,
#             "name": "Hamster",
#             "legs": 4,
#             "weight": 1.67,
#             "height":1.2,
#             "speed": 12,
#             "family": 3 
#         },
#         {
#             "id": 5,
#             "name": "Parrot",
#             "legs": 2,
#             "weight": 1.7,
#             "height":2.2,
#             "speed": 20,
#             "family": 4 
#         }
#     ],
#     "families": [
#         {
#             "id": 1,
#             "name": "Felidae"
#         },
#         {
#             "id": 2,
#             "name": "Caninae"
#         },
#         {
#             "id": 3,
#             "name": "Cricetidae"
#         },
#         {
#             "id": 4,
#             "name": "Psittacidae"
#         }
#     ]
# }
def read_data(location, key):
    with open(location, 'r') as file:
        data = json.load(file)
    sub_data = data[key]
    return sub_data
        
#     file['families'].write({'id': 3, 'name': 'Cricetidae'},{'id': 4, 'name': 'Psittacidae'})
  
# with open(filename, 'r') as file:
#     
# print(data)  

# Create your views here.


def families(request, id):
    info = []
    for i in read_data('data.json', 'animals'):
        if i['family'] == id:
            info.append(i['name'])
    return HttpResponse(f'{info}')
    
def animals(request, id):
    info = read_data('data.json', 'animals')[id-1]
    return HttpResponse(f'{info}')

            
