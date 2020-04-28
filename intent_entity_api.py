# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:59:08 2020

@Description: Entity Extraction and Intent Prediction Module

@author: rajakishorekavi
"""

from env import *

import en_core_web_sm
import requests
import os
import dialogflow
from google.api_core.exceptions import InvalidArgument

def get_entity(msg):
    
    nlp = en_core_web_sm.load()
    
    doc = nlp(msg)
    return doc 

def get_intent_luis(msg):
    
    website = LUIS_WEB_API+msg
    
    r = requests.get(url = website) 
    data  = r.json()
    
    return data['topScoringIntent']['intent']


def get_intent_dialogflow(msg):
       
    
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=msg, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise


    return response