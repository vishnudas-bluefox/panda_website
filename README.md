<h1 align=center>Panda_website<h1>

## An updated version of panda downloader to download contents from different social media social media
Supportted paltforms:
* Youtube
* Instagram
* Facebook
* Twitter

### Design File 
I just made a basic sketch using [Figma](https://www.figma.com/file/dXFR70vW82a2ricO2LIwLJ/Panda-downloader?node-id=0%3A1) to have a better idea of what the finished product would look like.

The django project runs locally :)

To run the django project on locally
* users need to cone the repo
```
git clone https://github.com/vishnudas-bluefox/panda_website.git
```
* getting inside of the cloned folder
```
cd panda_website
```
* creating a virtual environment for python dependencies
[ Notice: The below two commands aren't for windows users]
```
python3 -m venv venv
```
```
source venv/bin/activate/
```
install all the dependencies
```
pip install -r requirements.txt
```
run the backend server locally
```
cd backend
```
```
python3 manage.py runserver 
```
### if all the above statements works perfectly :relaxed: . open " frontend/pandadownloader.html " to use the beautiful frontend :heart_eyes:
# Youtube
 ![Youtube downloader](https://github.com/vishnudas-bluefox/panda_website/blob/master/screenshots/youtube.gif)
## Youtube API
-------------
### to fetch the details
```
http://localhost:8000/youtube/test/
```
used to fetch the details of videos and playlist
pass the url as a request body as json <br>
* requests.get("url",json={"url":"youtube-link"})

### to download a single video
```
http://localhost:8000/youtube/download/
```
json data
{
 url: "youtube-link",
 resolution: "144p",
}

* requests.get("url",json=data)
### to download a entire playlist
```
"http://localhost:8000/youtube/playlistdownload/"
```
json data
the response data +
{
  .......
  selected_resolution: "240p",
 }
 
  requests.get(downloadpoint,json=data)

# Instagram 
![Instagram downloader](https://github.com/vishnudas-bluefox/panda_website/blob/master/screenshots/instagram.gif)
 
## Instagram API
-------------
### for download the the posts & reels
```
http://localhost:8000/instagram/post_download/
```
### for download the profile picture
```
http://localhost:8000/instagram/profile_pic/
```
# Facebook
![Facebook downloader](https://github.com/vishnudas-bluefox/panda_website/blob/master/screenshots/facebook.gif)
 
## Facebook API
-------------
### download the post files
```
http://localhost:8000/facebook/post/
```

users can download the images directly from the facebook :)

# Twitter
![Twitter panda downloader](https://github.com/vishnudas-bluefox/panda_website/blob/master/screenshots/twitter.gif)
 
## Twitter API
-------------
### download tweet medi files 
```
http://localhost:8000/twitter/fetch/
```
