

import requests

endpoint = "http://localhost:8000/instagram/post_download/"



#for retrive the image data
get_response = requests.get(endpoint,json={"url":"https://www.instagram.com/p/Ckq9a5UIxTP/"})
print("Photo Link:")
print(get_response.json())

#for retrive the video data

get_response2 = requests.get(endpoint,json={"url":"https://www.instagram.com/p/Ck3uBuQAZgf/"})
print("Video_link:")
print(get_response2.json())
