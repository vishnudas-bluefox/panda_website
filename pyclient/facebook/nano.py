import requests

url = "https://facebook-reel-and-video-downloader.p.rapidapi.com/app/main.php"

querystring = {"url":"https://www.facebook.com/reel/1187362698778788"}

headers = {
	"X-RapidAPI-Key": "ce9aa27671mshf1664c1f586a149p1f3740jsn9be232d0ed69",
	"X-RapidAPI-Host": "facebook-reel-and-video-downloader.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
