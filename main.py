# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:45:54 2020

@Description: Main executable file. Run this file to run the application

@author: rajakishorekavi
"""

from wiki_api import *
from weather_api import *
from chatbot import *
from intent_entity_api import *
from env import *
from translate_api import *
from texttospeech_api import *


import pandas as pd
import numpy as np
import pickle
import re
import requests, json 

import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm

from nltk.chat.util import Chat, reflections

import wikipedia

from flask import Flask, request
from flask import render_template
from flask import jsonify

app = Flask(__name__)
msg = []

@app.route('/')
def hello():
    #msg.append("Hi, I'm chatbot. Ask me anything.")
    return render_template(HOME_PAGE_FILE, host_url=JAVASCRIPT_IP, port_num=ENV_PORT )

@app.route('/android/<message>/')
def android(message):
    reply = run_chatbot(message)
    return reply

@app.route('/api/', methods=["GET", "POST"])
def main_interface():
    if 'X-Forwarded-Proto' in request.headers and request.headers['X-Forwarded-Proto'] == 'https':
        return jsonify({'reply' : 'Error Inut Format'})
    else:
        response = request.get_json()
        msg = response['message']
        print(msg)
        msg = msg.replace("&nbsp;","")
        print(msg)
        msg_lng = detect_lang(msg)
        if msg_lng == 'te':
            msg = translate_lang(msg, 'en')
        print(msg)
        reply = run_chatbot(msg)
        print(reply)
        reply = translate_lang(reply, 'te')
        print(reply)
        #tts(reply)
        response.update({'reply': reply })
        return jsonify(response)

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response


if __name__ == '__main__':
    app.run()
