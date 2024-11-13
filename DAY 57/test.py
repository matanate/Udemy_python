import requests

response = requests.get(f"https://api.agify.io?name=matan")
age = response.json()["age"]

print(age)
