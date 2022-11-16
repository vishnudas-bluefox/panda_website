from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view


import requests

# Create your views here.
import os
from dotenv import load_dotenv

load_dotenv()

RapidAPI_key = os.getenv('rapidapi_key')



#api link
rapid_link = "https://facebook-reel-and-video-downloader.p.rapidapi.com/app/main.php"

headers = {
	"X-RapidAPI-Key": RapidAPI_key,
	"X-RapidAPI-Host": "facebook-reel-and-video-downloader.p.rapidapi.com"
}



@api_view(['GET'])
def post_fetch(request,*args,**kwargs):
    #url = request.GET['url']

    url = request.query_params.get('url')
    querystring = {"url":url}

    response = requests.request("GET", rapid_link, headers=headers, params=querystring)
    data = response.json()
    print(data)
    return Response(data)
