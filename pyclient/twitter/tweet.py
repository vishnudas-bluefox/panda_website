import requests
import json

endpoint = "http://localhost:8000/twitter/fetch/"

params = "url=https://twitter.com/engineers_feed/status/1592207414367252480"
response = requests.get(endpoint+"?"+params)

print(response.json())
