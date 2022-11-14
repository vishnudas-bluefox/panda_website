import requests

endpoint = "http://localhost:8000/facebook/post/"


get_response = requests.get(endpoint,json={"url":"test url"})

print(get_response.json())
