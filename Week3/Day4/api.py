import requests
import time
import json
database = []
while len(database) < 20:
    response = requests.get("http://api.open-notify.org/iss-now.json")
    # print(response)
    data = response.json()
    print(data)
    database.append(data)  
    time.sleep(0.5)
    
    filename= 'data.json'
    with open(filename, 'w') as file:
        json.dump(database, file)