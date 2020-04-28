# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:41:45 2020

@Description: Chatbot Replies for Basic Questions

@author: rajakishorekavi
"""

# Add msgs and replies as below.

pairs = [
        [
            r"my name is (.*)",
            ["Hello %1, How are you today ?",]
        ],
         [
            r"(what|wht) is (your|ur) name",
            ["My name is Chatty and I'm a chatbot ?",]
        ],
        [
            r"(how|hw) (are|r) (you|u) ?",
            ["I'm doing good. How about You ?",]
        ],
        [
            r"sorry (.*)",
            ["Its alright","Its OK, never mind",]
        ],
        [
            r"i'm (good|fine|ok)",
            ["Nice to hear that","Alright :)",]
        ],
        [
            r"hi|hey|hello",
            ["Hello", "Hey", "Hi" ]
        ],
        [
            r"(.*) age?",
            ["I'm a computer program dude\nSeriously you are asking me this?",]

        ],
        [
            r"what (.*) want ?",
            ["Make me an offer I can't refuse",]

        ],
        [
            r"(.*) created ?",
            ["Kishore created me using Python's NLTK library ","top secret ;)",]
        ],
        [
            r"(.*) (location|city) ?",
            ['Rajahmundry, AP',]
        ],
        [
            r"how (.*) health(.*)",
            ["I'm a computer program, so I'm always healthy ",]
        ],
        [
            r"quit",
            ["Bye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
        ],
        ]