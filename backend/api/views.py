from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
import json

from pytube import YouTube
# Create your views here.

def home(request):
    data= json.loads(request.body)
    url = data['Query']
    yt = YouTube(url).streams.filter(progressive=True).order_by("resolution")
    print(yt)
    return JsonResponse({"Message":"Success"})
