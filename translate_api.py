# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 16:34:19 2020

@Description: Translator

@author: rajakishorekavi
"""

from googletrans import Translator
from google.cloud import translate_v2 as translate
from env import *

#def translate_lang(msg, lang):

#    translator = Translator()
    
#    rply = translator.translate(msg, dest=lang)
    
#    return rply.text

def detect_lang(msg):
    
    translator =Translator()
    
    rply = translator.detect(msg)
    
    return rply.lang
    
def translate_lang(msg, lang):
    
    translate_client = translate.Client()
    
    rply = translate_client.translate(msg, target_language=lang)
    
    return rply['translatedText']