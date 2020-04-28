# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 16:31:57 2020

@Description: Covid19 API

@author: rajakishorekavi
"""

from env import *

import COVID19Py
import requests


def get_data_covid(msg, response):
    
    covid_data = requests.get(covidindia_api_url).json()
    
    country = response.query_result.parameters.fields['geo-country'].string_value
    state = response.query_result.parameters.fields['geo-state'].string_value
    district = response.query_result.parameters.fields['geo-city'].string_value
    
    print("Country:"+country+";")
    print("State:"+state+";")
    print("district:"+district+";")
    
    confirmed_cases = 0
    active_cases = 0
    deceased_cases = 0
    recovered_cases = 0
    location = ''
    
    if country == 'India' or country == 'india':
        
        confirmed_cases = 0
        active_cases = 0
        deceased_cases = 0
        recovered_cases = 0
        location = 'India'
        
        for i in list(covid_data.keys()):
            for j in covid_data[i]['districtData']:
                confirmed_cases += covid_data[i]['districtData'][j]['confirmed']
                active_cases += covid_data[i]['districtData'][j]['active']
                deceased_cases += covid_data[i]['districtData'][j]['deceased']
                recovered_cases += covid_data[i]['districtData'][j]['recovered']
        
        
    elif state != '':

        for i in covid_data[state]['districtData']:
            confirmed_cases += covid_data[state]['districtData'][i]['confirmed']
            active_cases += covid_data[state]['districtData'][i]['active']
            deceased_cases += covid_data[state]['districtData'][i]['deceased']
            recovered_cases += covid_data[state]['districtData'][i]['recovered']
        
        location = state
            
    elif district != '':
        
        state = ''
        for i in list(covid_data.keys()):
            for j in covid_data[i]['districtData']:
             #   print("i = "+i+" ; j ="+j.lower().replace(" ","")+"; district="+district.lower().replace(" ","")+" ;")
             # Character "\xa0" is in between spaced words from entites from Dialog flow. So removing it.
                if j.lower().replace(" ","").find(district.lower().replace("\xa0","")) != -1 or j.lower().replace(" ","") == district.lower().replace("\xa0","") :
                    
                    state = i
                    location = district
                    district = j
                    break
            if state != '':
                break
        
        print("State="+state+";District="+district+";Location="+location)
        
        if state != '':
            confirmed_cases += covid_data[state]['districtData'][district]['confirmed']
            active_cases += covid_data[state]['districtData'][district]['active']
            deceased_cases += covid_data[state]['districtData'][district]['deceased']
            recovered_cases += covid_data[state]['districtData'][district]['recovered']
        
            
    else:
        
        location = ''
        
    return { 'cc' : confirmed_cases,
             'ac' : active_cases,
             'dc' : deceased_cases,
             'rc' : recovered_cases,
             'loc' : location }