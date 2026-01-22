import requests

id = int(input(" Digite o ID desejado: "))

response = requests.get("https://thesimpsonsapi.com/api/characters")
data = response.json()

print(data.get("results")[id].get("name"))
print(data.get("results")[id].get("birthdate"))
print(data.get("results")[id].get("gender"))
print(data.get("results")[id].get("occupation"))


