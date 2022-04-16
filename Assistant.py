import pyttsx3
import speech_recognition as sr
import datetime
import sys
import time
import wikipedia
from requests import get
import os
import pywhatkit


pyttsx3.init()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():  # It takes microphome input and provides string output


    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening....") 
        r.pause_threshold = 0.5
        audio=r.listen(source)

    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language='en-us') 
        print(f"User said: {query}\n")

    except Exception as e:
        print(e) 
        return "None" 

    query = query.lower()
    return query

def wishMe():
    hour = int(datetime.datetime.now().hour)

    time.sleep(1)
    
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon")      

    elif hour>=18:
        speak("Good Evening")
    

    speak("I am Gideon. Please tell me how may I help you?") 


def Task_Gui():
    
    wishMe()

    while True:
        query = takeCommand()

        if 'exit' in query:
            print("Exiting Sir, Have a nice day.")
            speak("Exiting Sir, Have a nice day.")
            sys.exit()

        elif "my ip address" in query:
            try:
                ip = get('https://api.ipify.org').text
                print(f"Your IP Address is {ip}")
                speak(f"Your IP Address is {ip}")
            except Exception as e:
                print(e)            
                speak("No Internet connection")            

        elif 'wikipedia' in query:
            speak('Searching Wikipedia sir...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query ,sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif "open google" in query:
            print("What should I search on google?")
            speak("What should I search on google?")
            gsearch = takeCommand().lower()
            pywhatkit.search(f"{gsearch}")
        
        elif "open youtube" in query:
            print("What should I play on Youtube?")
            speak("What should I play on youtube?")
            yt_search = takeCommand().lower()
            print(f"User said: {yt_search}")
            pywhatkit.playonyt(f"{yt_search}")

        elif "open cmd" in query:
            os.system("start cmd")

        elif "open command prompt" in query:
            os.system("start cmd")        

        elif "current working directory" in query:
            cwd = os.getcwd()
            print(f"Your current working directory is: {cwd}")
            speak(f"Your current working directory is: {cwd}")

        elif "present working directory" in query:
            cwd = os.getcwd()
            print(f"Your current working directory is: {cwd}")
            speak(f"Your current working directory is: {cwd}")

        else:
            pass
