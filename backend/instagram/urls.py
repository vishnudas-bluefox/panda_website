#!/usr/bin/env python3
#

from django.urls import path

from . import views

urlpatterns = [
    path('post_download/',views.fetch_post),
    path('profile_pic/',views.profile_pic)
]
