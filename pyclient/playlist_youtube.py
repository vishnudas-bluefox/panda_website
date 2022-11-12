import requests

endpoint = "http://localhost:8000/youtube/test/"

url = "https://youtube.com/playlist?list=PLFZcKl7gjg4H7RCtVzarMvVoOv7nOBTss"
result = requests.get(endpoint,json={"url":url})

print(result.json())
