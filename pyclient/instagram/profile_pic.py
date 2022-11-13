import requests

username = "charvaakan"

endpoint = "http://localhost:8000/instagram/profile_pic/"

get_response = requests.get(endpoint, json={"username":username})

print(get_response.json()) 
