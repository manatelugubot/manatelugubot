# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:46:52 2020

@Description: Wikipedia API Module

@author: rajakishorekavi
"""
import wikipedia
import re

def wiki(msg, response):
    
    if response.query_result.parameters.fields['any'].string_value != '':
        
        search_word = response.query_result.parameters.fields['any'].string_value
        
    elif response.query_result.parameters.fields['person'].string_value != '':
        
        search_word = response.query_result.parameters.fields['person'].string_value
        
    else:
        
        search_word = msg.lower()
        
        replace_words = ["what is ", "information about ", "explain ", " about ", "describe ", " info ", "who is ", "get me some ", "get me "]
        
        for i in replace_words:
            search_word = search_word.replace(i, "")
    
    wikisearch = ""
    
    try:

        wikisearch = wikipedia.summary(wikipedia.search(search_word)[0])

    except:

        try:
            wikisearch = wikipedia.summary(wikipedia.suggest(search_word))
  
        except:
            
            wikisearch = "Seems like its difficult for me to find. Please ask something else."
    
    if wikisearch != "":
        matches = re.finditer("\.", wikisearch)
        dot_indexes = [match.start() for match in matches]
        if dot_indexes[1] > 100 :
            indx = dot_indexes[0]+1
        else:
            indx = dot_indexes[1]+1
                
        wikisearch = wikisearch[0:indx]
    
    return wikisearch
