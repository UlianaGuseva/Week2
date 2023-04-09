import requests
response = requests.get("https://api.chucknorris.io/jokes/random?category=explicit")
data = response.json()
print(data)
