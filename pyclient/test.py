import requests

# check the url fetch data test
endpoint ="http://localhost:8000/youtube/test/"
url= "https://youtu.be/AC0vNGQIdLs"

get_response = requests.get(endpoint,json={"url":url})

print(get_response.json())


#download the above data

data = {}
data["url"] = url
data["resolution"] = "144p"
endpoint2 ="http://localhost:8000/youtube/download/"
get_download_link = requests.get(endpoint2,json=data)

print(get_download_link.json())
