# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:54:23 2020

@Description: Weather API Module

@author: rajakishorekavi
"""

from env import *

import requests


def get_weather(loc):
     
    city_name = loc
  
    complete_url = weather_api_url + "APPID=" + weather_api_key + "&q=" + city_name 
  
    response = requests.get(complete_url)
    
    x = response.json() 
    
    if x["cod"] != "404": 
        y = x["main"] 
    else:
        return loc+" not found. Please try again"

    return { 'temp':round(y["temp"] - 273.15, 1), 'description': x["weather"][0]["description"], 'location': loc }

def get_location():
    
    send_url = ipstack_api_url+ipstack_api_key
    
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']
    city = geo_json['city']
    
    return city