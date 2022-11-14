#!/usr/bin/env python3

from django.urls import path
from . import views


urlpatterns = [
    path('post/',views.post_fetch),
]
