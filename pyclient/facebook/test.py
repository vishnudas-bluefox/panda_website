#!/usr/bin/env python3

import requests
import re


url = "https://fb.watch/gMCB7vjEws/"

page_source = requests.get(url)

#parsing url
data ={}
try:
    data['type']="HD"
    url = re.search('hd_src:"(.+?)"',page_source.text)
except:
    data['type']="SD"
    url = re.search('sd_src:"(.+?)"',page_source.text)

print(data)
