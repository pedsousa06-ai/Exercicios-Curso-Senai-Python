import requests 
id = int(input(" Qual é valor da id: "))

response = requests.get("https://rickandmortyapi.com/api/character")
data = response.json()

print(data.get("results")[id].get("name"))
print(data.get("results")[id].get("status"))
print(data.get("results")[id].get("species"))
print(data.get("results")[id].get("type"))


