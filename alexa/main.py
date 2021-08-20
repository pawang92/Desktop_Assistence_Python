import pyjokes
import speech_recognition as sr
import pyttsx3
import pywhatkit as py
import datetime
import wikipedia
import wolframalpha
import tkinter
import random
import operator
import webbrowser
import os
import winshell
import feedparser
import smtplib
import ctypes
# import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from bs4 import BeautifulSoup
# import win32com.client as wincl
from urllib.request import urlopen

listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


engine = pyttsx3.init()
engine.say(' Hi I am your alexa')
engine.say('what can i do for you')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        py.playonyt(song)
    elif 'search' in command:
        search = command.replace('search', '')
        talk('searching' + search)
        py.search(search)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Sorry, I have headache')
    elif 'are you single' in command:
        talk('i am in a relationship with wifi')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(joke)
    elif 'open google' in command:
        talk('Here you go to google\n')
        webbrowser.open("google.com")
    elif 'open map' in command:
        talk('map is opening\n')
        webbrowser.open('https://www.google.co.in/maps?hl=en&tab=rl')
    elif 'who are you' in command:
        talk('I am your virtual assistant created by Pawan kumar')
    elif 'is love' in command:
        talk('it is 7th sense that destroy all other senses')
    elif 'lock window' in command:
        talk('locking the device')
        ctypes.windll.uint32.LockWorkStation()
    elif 'empty recycle bin' in command:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
        talk('Recycle bin recycled')
    elif 'Exit' in command:
        talk('thanks for giving me your time')
        exit()
    else:
        talk('Please say the command again')


while True:
    run_alexa()
