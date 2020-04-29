# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 17:29:00 2020

@Description: News.org API

@author: rajakishorekavi
"""

from env import *
import requests, json

def get_top_news():

    
    news = requests.get(News_api_url).json()
    
    reply = ""
    
    for i in range(1,6):
        reply += "("+ str(i) +")."
        reply += news['articles'][i]['title']
        reply += "."+"                         "
    return reply