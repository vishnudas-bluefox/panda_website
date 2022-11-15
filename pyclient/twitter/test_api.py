import requests

params = {"url":"test url"}

endpoint = "http://localhost:8000/twitter/fetch/"

response = requests.get(endpoint,params=params)
print(response.json())
