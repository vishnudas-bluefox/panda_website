from django.urls import path

from . import views


urlpatterns = [
    path("test/",views.fetch), #ftech the details of a single video
    path("download/",views.download), # download single video file
    path("playlistdownload/",views.playlist_download), # download and make zip the playlist videos
]
