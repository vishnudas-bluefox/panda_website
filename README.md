<h1 align=center>Panda_website<h1>

## An updated version of panda downloader to download contents from different social media social media
Supportted paltforms:
* Youtube
* Instagram
* Facebook
* Twitter

### Design File 
I just made a basic sketch using [Figma](https://www.figma.com/file/dXFR70vW82a2ricO2LIwLJ/Panda-downloader?node-id=0%3A1) to have a better idea of what the finished product would look like.

Youtube API
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
