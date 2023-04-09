import json

filename = 'data.json'
data = {}

with open(filename, 'r') as file:
    data = json.load(file)
    
print(data)