from django.shortcuts import render

import requests
import json
import os
from dotenv import load_dotenv

from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

load_dotenv()
RapidAPI_key = os.getenv('rapidapi_key1')

@api_view(['GET'])
def fetch(request,*args,**kwargs):

    url2 = request.query_params.get('url')
    url = "https://socialdownloader.p.rapidapi.com/api/twitter/video"
    querystring = {"video_link":url2}
    headers = {
	    "X-RapidAPI-Key": RapidAPI_key,
	    "X-RapidAPI-Host": "socialdownloader.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()


    #for testing the api
    #with open("sample.json", "w") as outfile:
     #   outfile.write(data)
    #with open("sample.json", "r") as f:
     #   data = json.load(f)
    try:
        data_text = data["body"]["user"]["text"].split(" ")
        data["tweet_url"] = data_text[-1]
        temp = data_text.pop(-1)
        data["tweet_name"]= ' '.join([str(elem) for elem in data_text])
    except:
        pass
    print(data)
    return Response(data)
