#!/usr/bin/env python3

import requests

endpoint= "http://localhost:8000/api/"

url = "https://www.youtube.com/watch?v=M-Jz2njxSxg"
get_response = requests.get(endpoint,json={"Query":url})

print(get_response.json())
