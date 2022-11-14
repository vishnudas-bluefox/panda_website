from django.shortcuts import render

import json
#importing rest_framework modules
from rest_framework.decorators import api_view
from rest_framework.response import Response
#importing pytube modules
from pytube import YouTube,Playlist
from django.http import JsonResponse


# to fetch the datas from youtube
@api_view(['GET','POST'])
def fetch(request,*args,**kwargs):
    print(request.body)
    #check the metod of request
    #if request.method != "GET":
        #return Response({"Error":"Get was the only request method available here"})
    body = json.loads(request.body)
    url =body['url']

    # was the link playlist or not
    flag = check(url)
    if flag is True:
        playlist_details = fetchplaylist(url)
        return Response(playlist_details)
    else:
        available_streams = fetchdata(url)
        print(available_streams)
        return Response(available_streams)
# to download the videos contentsfrom youtube

@api_view(['GET'])
def download(request,*args,**kwargs):
    if request.method != "GET":
        return Response({"Error":"Get was the only request method available here"})
    data =json.loads(request.body)
    url=data["url"]
    resolution=data["resolution"]

    yt = YouTube(url)
    try:
        try:
            yt.streams.filter(progressive=True, resolution=resolution).first().download("youtube/downloads")
        except:
            yt.streams.filter(progressive= True).order_by('resolution').desc().first().download("youtube/downloads")
    except:
        return Response({"Error":"Panda is facing some issues to download your file"})
    return Response({"Message":"Success"})


@api_view(["GET"])
def playlist_download(request,*args,**kwargs):
    if request.method != "GET":
        return Response({"Error":"Get was the only request method available here"})
    data = json.loads(request.body)
    #download all the playlist videos
    url = data["download_url"]
    yt = YouTube(url)
    try:
        yt.streams.filter(progressive = True , resolution = data["selected_resolution"]).first().download("youtube/downloads/"+data["playlist_title"])
    except:
        yt.streams.filter(progressive = True).order_by('resolution').desc().first().download("youtube/downloads/"+data["playlist_title"])


    # increment downloaded files

    # create zip file


    return Response({"files_downloaded":data["downloaded_videos"]})




def check(url):
    try:
        p = Playlist(url)
        length = len(p)
        if length>1:
            return True
        else:
            return False
    except:
        return False
#@api_view(["GET"])
def fetchplaylist(url):
    #url = json.loads(request.body)["url"]
    p = Playlist(url)
    data = {}
    urls=[]

    for video_urls in p.video_urls:
        urls.append(video_urls)

    # available resoltions of video

    yt = YouTube(urls[0])
    resolution_list=[]

    for stream in yt.streams.order_by('resolution').desc():

        res= stream.resolution

        if res in resolution_list:
            pass
        else:
            resolution_list.append(res)


    data["playlist_title"] = p.title
    data["playlist_url"] = url
    data["no_of_videos"] = len(p)
    data["video_urls"] = urls
    data["available_resolutions"] = resolution_list
    data["playlist_id"] = p.playlist_id
    return data

#to fetch the data from url
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
    data["Video_url"] = url
    data["resolutions"] = resolution_list
    return data
