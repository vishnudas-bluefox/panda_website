import requests

# check the url fetch data test
endpoint ="http://localhost:8000/youtube/test/"
url= "https://youtube.com/playlist?list=PLFZcKl7gjg4H7RCtVzarMvVoOv7nOBTss"

get_response = requests.get(endpoint,json={"url":url})

data =  get_response.json()


selected_resolution = "144p"
data["selected_resolution"] =selected_resolution

# download and make a zip file of playlist
downloadpoint = "http://localhost:8000/youtube/playlistdownload/"

# current_downloaded video
data["downloaded_videos"]=1
for i in  data["video_urls"]:
    data["download_url"] = i
    get_response = requests.get(downloadpoint,json=data)
    data["downloaded_videos"] +=1
    print(get_response.json())

# select available resolutions 
#``print(get_response.json())
