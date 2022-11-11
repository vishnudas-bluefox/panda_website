from django.shortcuts import render

import json
#importing rest_framework modules
from rest_framework.decorators import api_view
from rest_framework.response import Response
#importing pytube modules
from pytube import YouTube
from django.http import JsonResponse


# to fetch the datas from youtube
@api_view(['GET'])
def fetch(request,*args,**kwargs):

    #check the metod of request
    if request.method != "GET":
        return Response({"Error":"Get was the only request method available here"})
    body = json.loads(request.body)
    url =body['url']
    available_streams = fetchdata(url)
    print(available_streams)
    return Response({"Message":"success"})



def fetchdata(url):
    yt = YouTube(url)
    progressive_files = yt.streams.filter(progressive=True)
    data={}
    resolution_list = []
    for stream in yt.streams.order_by('resolution'):

        res= stream.resolution

        if res in resolution_list:
            pass
        else:
            resolution_list.append(res)

    # adds videos data to data dictionary
    data["title"] = yt.title
    data["tumbnail_url"] = yt.thumbnail_url
    data["resolutions"] = resolution_list
    return data
