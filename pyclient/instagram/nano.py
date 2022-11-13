import requests
import re

import json
import os
from dotenv import load_dotenv

import instaloader


load_dotenv()
username = os.getenv('NAME')
password = os.getenv('PASSWORD')

def get_response(url):
    r = requests.get(url)
    while r.status_code != 200:
        r = requests.get(url)
    return r.text


def prepare_urls(matches):
    return list((match.replace("\\u0026","&") for match in matches))


def main():
    url = "https://www.instagram.com/p/CkxRWyhvImU/"
    response = get_response(url)
    vid_matches = re.findall('"video_url":"([^""])"',response)
    pic_matches = re.findall('"display_url":"([^""])"',response)
    print(vid_matches,pic_matches)
    vid_urls = prepare_urls(vid_matches)
    pic_urls = prepare_urls(pic_matches)


    if vid_urls:
        print("Videos Detected:\n[0]".format("\n".join(vid_urls)))

    if pic_urls:
       print("Videos Detected:\n[0]".format("\n".join(pic_urls)))


    if not(vid_urls or pic_urls):
        print("not valid urls")





def test():
    L = instaloader.Instaloader()
    print(username,password)
# Optionally, login or load session
    L.login(username,password)        # (login)
    post_url = "https://www.instagram.com/reel/CkzSII2LpIP/?utm_source=ig_web_copy_link"
    post = instaloader.Post.from_shortcode(L.context, post_url.split('p/')[1].strip('/ '))
    photo_url = post.url   # this will be post's thumbnail (or first slide)
    video_url = post.video_url
    print(photo_url,video_url)



def scrape_kunt():
    url = "https://www.instagram.com/p/CkvEHOihzJk/"
    post_data = url.split('/')
    post_id=post_data[4]
    format_link = f"https://api.zenrows.com/v1/?apikey=813dcf383caedb54fe88f33a4686420821113c5f&url=https%3A%2F%2Fwww.instagram.com%2Fp%2F{post_id}%2F%3Futm_source%3Dig_web_copy_link&js_render=true&premium_proxy=true&autoparse=true"

    response = requests.get(format_link)

    data = response.json()


    image_link = data['shortcode_media']['display_url']
    try:
        video_image= data['shortcode_media']['display_url']
        video_link = data['shortcode_media']['video_url']
    except:
        video_link = None

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
    f.close()

scrape_kunt()

#parse json contents

def parse():
    with open("data.json","r") as readfile:
        data=readfile.readlines()
    list = ''.join(data)
    data = json.loads(list)
    print(data['shortcode_media']['video_url'])
