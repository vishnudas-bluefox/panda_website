import requests

# check the url fetch data test
endpoint ="http://localhost:8000/youtube/test/"
url= "https://youtu.be/AC0vNGQIdLs"

get_response = requests.get(endpoint,json={"url":url})

print(get_response.json())
