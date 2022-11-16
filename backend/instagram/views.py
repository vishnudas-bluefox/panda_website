from django.shortcuts import render

import json
#importing rest_framework modules
from rest_framework.decorators import api_view
from rest_framework.response import Response

# for scrapping contents fron instagram
import instaloader
import requests

#fetch the post details
@api_view(['GET'])
def fetch_post(request,*args,**kwargs):

    print("request successfull")
    #req_body=json.loads(request.body)
    url = request.query_params.get('url')
    print(url)
    post_data = url.split('/')
    print(post_data)
    post_id=post_data[4]
    format_link = f"https://api.zenrows.com/v1/?apikey=4c231f11b73d3297335473dfa6d95be3eeac9b2b&url=https%3A%2F%2Fwww.instagram.com%2Fp%2F{post_id}%2F%3Futm_source%3Dig_web_copy_link&js_render=true&premium_proxy=true&autoparse=true"
    response = get_post_data(format_link)
    print("response gotted!")
    print(response)
    data = response.json()
    data_return = {}
    print("parsing the links")

    #creating link from json response
    try:
        data_return['video_link'] = data['shortcode_media']['video_url']
        data_return['video_tumbnail']= data['shortcode_media']['display_url']
        print(data_return)
    except:
        data_return['image_link'] = data['shortcode_media']['display_url']
        data_return['video_link'] = None
        data_return['video_tumbnail'] = None
        print("except",data_return)


    return Response(data_return)

@api_view(['GET'])
def profile_pic(request,*args,**kwargs):
    data = json.loads(request.body)
    print(data)
    ig = instaloader.Instaloader()
    dp = data['username']

    ig.download_profile(dp , profile_pic_only=True,)

    return Response({"Message":"success"})
def get_post_data(format_link):
    response = requests.get(format_link)
    return response
