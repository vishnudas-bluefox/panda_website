from django.shortcuts import render

import requests

import os
from dotenv import load_dotenv

from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

load_dotenv()
RapidAPI_key = os.getenv('rapidapi_key')

@api_view(['GET'])
def fetch(request,*args,**kwargs):
    url2 = request.GET["url"]

    url = "https://socialdownloader.p.rapidapi.com/api/twitter/video"
    querystring = {"video_link":url2}
    headers = {
	    "X-RapidAPI-Key": RapidAPI_key,
	    "X-RapidAPI-Host": "socialdownloader.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    return Response(data)
