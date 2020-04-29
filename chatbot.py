# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:56:32 2020

@Description: To Run the Chatbot and get the responses.

@author: rajakishorekavi
"""

from wiki_api import *
from weather_api import *
from intent_entity_api import *
from env import *
from basic_msgs import *
from covid_api import *

import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm

from nltk.chat.util import Chat, reflections

def run_chatbot(msg):
    

    chat = Chat(pairs, reflections)

    rply = chat.respond(msg.lower())
    
    if rply != None:
        return rply
    else:
 
        #model, vect = get_model_vect(model_file_name, vect_file_name)
        #msg_list = []
        #msg_list.append(msg)
        #trans_msg = vect.transform(msg_list)
        #intent = model.predict(trans_msg)
        
        #intent = get_intent_luis(msg)
        response = get_intent_dialogflow(msg)
        
        if response.query_result.action.find('smalltalk') != -1 :
            if response.query_result.fulfillment_text != '':
                return response.query_result.fulfillment_text
            else:
                return "I don't have reply for this. I'll ask my developer to add one."
    
        intent = response.query_result.intent.display_name
        #insert_msg_intent(msg, intent)
        print(intent)
    
        if intent == 'weather' :

            loc = ''
            loc = response.query_result.parameters.fields['geo-city'].string_value

            if loc == '' or loc == None:
                loc = get_entity(msg)
                if loc == '' or loc == None:
                    return "Location not found. Please try again"

            weather_result = get_weather(loc)

            weather_reply = "The weather in "+loc+" is "+str(weather_result['temp'])+" degrees with "+weather_result['description']

            if msg.find("raining") != -1 :
                if weather_result['description'].find("rain") != -1:
                    weather_reply = "Yes. Its "+weather_result['description']+" with "+str(weather_result['temp'])+" degrees"
                else:
                    weather_reply = "No. It's not raining. Currently the temperature in "+loc+" is "+str(weather_result['temp'])+" degrees"


            return weather_reply

        elif intent == 'wikipedia' :

            return wiki(msg, response)
        
        elif intent == 'covid' :
            
            api_output = get_data_covid(msg, response)
            
            if msg.lower().find('active') != -1:
                
                return "Total Corona Active cases in "+api_output['loc']+" are "+str(api_output['ac'])
            
            elif msg.lower().find('died') != -1 or msg.lower().find('deceas') != -1 :
                
                return "Total Corona Deceased cases in "+api_output['loc']+" are "+str(api_output['dc'])
            
            elif msg.lower().find('recover') != -1 or msg.lower().find('recovered') != -1 :
                
                return "Total Corona Recovered cases in "+api_output['loc']+" are "+str(api_output['rc'])
            
            elif msg.lower().find('confirm') != -1 or msg.lower().find('confirmed') != -1 :
                
                return "Total Corona Confirmed cases in "+api_output['loc']+" are "+str(api_output['rc'])
            
            else:
                
                if api_output['loc'] != '':
                    return "Corona Cases in "+api_output['loc']+":  Active cases = "+str(api_output['ac'])+" ; Confirmed cases = "+str(api_output['cc'])+" ; Deceased cases = "+str(api_output['dc'])+" ; Recovered cases = "+str(api_output['rc'])
                else:
                    return "As of now, I can only get details of States and Districts from India only."
                
        elif intent =='news' :
            
            return get_top_news()
        
        else :
            
            return "I'm still in Beta. This feature will be coming soon"