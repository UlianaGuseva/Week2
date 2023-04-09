import json

data = {
    'weather': 'cool',
    'temp': 234,
    'numb': [1,2,3,4]
}

filename = 'data.json'

with open(filename, 'w') as file:
    json.dump(data, file)