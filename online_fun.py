import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config


def search_on_wikipedia(query):
    results=wikipedia.summary(query,sentences=2)
    return results

def play_on_youtube(video):
    kit.playonyt(video)

def search_on_google(query):
    kit.search(query)

def get_jokes():
    headers={
        'Accept':"application/json"

    }
    res=requests.get("https://icanhazdadjoke.com/",headers=headers).json()
    return res['joke']

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']


def get_song(song):
    kit.playonyt(song)

def send_whatsapp_msg(number,message):
    kit.sendwhatmsg_instantly(f"{number}",message)