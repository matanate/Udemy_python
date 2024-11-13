import requests
from datetime import datetime

USERNAME = "matanate"
TOKEN = "nkln3n4jn3kn"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
headers = {"X-USER-TOKEN": TOKEN}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"

today = datetime(year=2023, month=9, day=1)
today = today.strftime("%Y%m%d")
pixel_config = {"date": today, "quantity": "25"}
response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)
