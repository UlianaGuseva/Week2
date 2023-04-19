import requests
import json
database = []
while len(database) < 10:
    
    response = requests.get(https://restcountries.com/)
    data = response.json()
    print(data)
    database.append(data)
print(database)
    
    