import requests
import json


body = {
    "rate": "usd",
    "value": 12.5
}
Server_url = "http://127.0.0.1:5000/api/getRates/"
response = requests.post(Server_url, json=body)
print(response.text)
