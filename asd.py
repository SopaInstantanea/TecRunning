from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import shutil
import os
import subprocess
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEngineView, QWebEnginePage
import urllib.request
from difflib import SequenceMatcher as SM
api_key = "AIzaSyDOzUn63at_ih3n77vX2lzYlX0jRc_gnYo"
from apiclient.discovery import build
youtube = build('youtube', 'v3', developerKey=api_key)
req = youtube.search().list(part='snippet',q="hola soy german",type='playlist')#type='channel'
type(req)
res = req.execute()
#print(str(res).encode('unicode-escape').decode('utf-8'))
for videos in res["items"]:
#-----------------------------------------------------------------------------------------------
    miniaturaURL = videos["snippet"]["thumbnails"]["default"]["url"].split("/")
    print(miniaturaURL[4])
    
