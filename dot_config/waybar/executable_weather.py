#!/usr/bin/python

import subprocess
from pathlib import Path
import json
import pickle
import time
import threading
import requests
from bs4 import BeautifulSoup

OUT = f"{Path.home()}/.config/hypr/store/dynamic_out.txt"
# PREV_PATH = f"{Path.home()}/.config/hypr/store/prev.txt"
prev = None

city = "sergiyev posad"
 
# creating url and requests instance
url = "https://www.google.com/search?q="+"weather"+city+"&hl=en"
html = requests.get(url).content

def print(ar):
    with open(OUT,"w") as f:
        f.write(json.dumps(ar))

# with open(f"{Path.home()}/.config/hypr/im_here","w") as f:
#     f.write("")

global PAUSE_MEDIA
PAUSE_MEDIA = False

def notif_watcher():
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str_temp = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    data = str_temp.split('\n')
    sky = data[1]
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text
    pos = strd.find('Wind')
    other_data = strd[pos:]
    print({"class": "playing", "text": f"{sky.lower()} {temp}"})
    time.sleep(60)


def start_watcher():
    while 1:
        notif_watcher()
        time.sleep(0.5)

t = threading.Thread(target=start_watcher)
t.start()
t.join()
