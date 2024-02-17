import pyttsx3
from decouple import config
from datetime import datetime
import speech_recognition as sr
from random import choice
from utils import opening_text
import os
import requests
import pyaudio
from functions import online_fun,offline_ops
from functions.online_fun import get_song
from pprint import pprint

USERNAME=config("USER")
BOTNAME=config("BOTNAME")

speechengine=pyttsx3.init('sapi5')

speechengine.setProperty('rate',190)

speechengine.setProperty('volume',1.0)

voices=speechengine.getProperty('voices')
speechengine.setProperty('voice',voices[1].id)

def talk(text):
    speechengine.say(text)
    speechengine.runAndWait()

def addres_user():

    hour=datetime.now().hour
    if (hour>=6) and (hour<12):
        talk(f"Good Morning {USERNAME}")
    elif (hour>=12) and (hour<16):
        talk(f"Good Afternoon {USERNAME}")
    elif (hour>=16) and (hour<19):
        talk(f"Good Evening {USERNAME}")
    elif (hour>19) and (hour<=24):
        talk(f"Hello {USERNAME} lovely night isn't it")
    talk(f"I am {BOTNAME}. How may I assist you?")


def take_input():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening your command.....')
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        print("Recognizing your voice...")
        #r.adjust_for_ambient_noise(source)
        query=r.recognize_google(audio,language='en-in')
        if not 'exit' in query or 'stop' in query:
            talk('Please wait a moment sir!!')
        else:
            hour=datetime.now().hour
            if hour >=21 and hour <6:
                talk("Good night sir, Take car!")
            else:
                talk("have a good day sir!")
            exit()
    except Exception:
        talk("Sorry , I could not understand. Could you please say that again!")
        query="None"
    return query 

if __name__=='__main__':
    addres_user()
    while True:
        query=take_input().lower()

        if 'open notepad' in query:
            offline_ops.open_notepad()
        
        elif 'open camera' in query:
            offline_ops.open_camera()
        
        elif 'open command prompt'in query:
             offline_ops.open_cmd()
        
        elif 'tell me about wikipedia' in query:
            talk('What do you want to search on Wikipedia, sir?')
            search_query = take_input().lower()
            results = online_fun.search_on_wikipedia(search_query)
            talk(f"According to Wikipedia, {results}")
            talk("For your convenience, I am printing it on the screen sir.")
            print(results)
            
        
        elif 'play a video on youtube' in query:
            talk('what do you want to play on youtube, sir?')
            video =take_input().lower()
            online_fun.play_on_youtube(video)
            
        
        elif 'search on google' in query:
            talk("What do you want to search on google, sir?")
            query=take_input().lower()
            online_fun.search_on_google(query)
            

        elif 'make me laugh' in query:
            talk("Hope you like it..")
            joke=online_fun.get_jokes()
            talk(joke)
            talk('For your convenience, I am printing it on the screen')
            pprint(joke)

        elif 'tell me a fun fact' in query:
            talk("here is a fun fact for you,sir")
            advice=online_fun.get_random_advice()
            talk(advice)
            talk('For your convenince i am printing it on the screen')
            pprint(advice)
        
        elif f'play song' in query:
            talk("what song do you want to listen!!")
            song=take_input().lower()
            talk("here you go enjoy!!")
            get_song(song)
            
        elif 'transcribe what i say' in query:
            talk("Ohk sir..!")
            speech=take_input()
            print(speech)

        elif 'open telegram' in query:
            talk("just a moment sir")
            offline_ops.open_telegram

        elif "send whatsapp message" in query:
            talk(
                'On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            talk("What is the message sir?")
            message = take_input().lower()
            online_fun.send_whatsapp_msg(number, message)
            talk("I've sent the message sir.")

