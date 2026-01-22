import requests

id = int(input(" Digite o id do personagem: "))

response = requests.get("https://dragonball-api.com/api/characters")
data = response.json()

print(data.get("items")[id].get("name"))
print(data.get("items")[id].get("ki"))
print(data.get("items")[id].get("maxKi"))
print(data.get("items")[id].get("race"))
print(data.get("items")[id].get("gender"))