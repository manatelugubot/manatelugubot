# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:40:00 2020

@Description : Text to Speech Conversion

@author: rajakishorekavi
"""

from gtts import gTTS 
from google.cloud import texttospeech
from env import *
  
"""
def tts(msg):
    
    print("Text to Speech Started")
    myobj = gTTS(text=msg, lang='te', slow=False) 
    print("Text to Speech Finished")
    
    #myobj.save(audio_file_loc+"gtts_out.mp3") 
    #print("Saving Audio file)
    print(myobj.get_urls())
    #return myobj.get_urls()
    
    return myobj.get_urls()
    
"""

def tts(msg):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()
    
    # Set the text input to be synthesized
    synthesis_input = texttospeech.types.SynthesisInput(text=msg)
    
    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='te-IN',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)
    
    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)
    
    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    
    # The response's audio_content is binary.
    with open(audio_file_loc+'output.mp3', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file "output.mp3"')