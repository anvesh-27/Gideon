import pyttsx3
import speech_recognition as sr
import datetime
import sys
import time
import wikipedia
from requests import get
import os
import pywhatkit
import wolframalpha

try:
    app = wolframalpha.Client("48RLHU-QAT37WAXH8")

except:
    print("Internet connention error")

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
        query = r.recognize_google(audio, language='en-in') 
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
wishMe()
print("I can take both text as well voice input. \nYou just need to type '1' for text input or type '2' for voice input.")
speak("I can take both text as well voice input. \nYou just need to type '1' for text input or type '2' for voice input.")
ip = int(input())

if ip==1:
    if __name__ == "__main__":
        while (True):
                speak("How can I help you?")
                query = input("How can I help you?")
                

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
                    try:
                        speak("Searching wikipedia.....")
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=5)
                        speak("According to wikipedia")
                        print(results)
                        speak(results)
                    except Exception as e:
                        print("An Error Occured!")
                        speak("An Error Occured!")


                elif "open google" in query:
                    print("What should I search on google?")
                    speak("What should I search on google?")
                    gsearch = input()
                    pywhatkit.search(f"{gsearch}")

                elif "open youtube" in query:
                    print("What should I play on Youtube?")
                    speak("What should I play on youtube?")
                    yt_search = input()
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

                elif 'who are you' in query:
                    speak("I am a basic AI Technology based prototype named Gideon sir...")
                    print("I am a basic AI Technology based prototype named Gideon sir...")

                elif 'your name' in query:
                    speak("My name is Gideon.")
                    print("My name is Gideon.")

                elif 'you have feelings' in query:
                    speak("Yes sir, I have lots of emotions. I feel excited when I learn something new.")
                    print("Yes sir, I have lots of emotions. I feel excited when I learn something new.")

                elif 'you like me' in query:
                    speak("I like you even more than anything else sir..." )
                    print("I like you even more than anything else sir..." )

                    # elif 'switch to voice mode' in query:
                    #     ip = ip+1
                    #     break
                        
                else:
                    print(f"Would you like me to search {query} on google?")
                    speak(f"Would you like me to search {query} on google?")
                    # z = takecommand().lower()
                    X = str(input())
                    if "yes" in X:
                        try:
                            speak("Searching.....")
                            query = query.replace("wikipedia", "")
                            results = wikipedia.summary(query, sentences=3)
                            speak("According to wikipedia")
                            print(results)
                            speak(results)
                        except Exception as e:
                            print("No result found!")
                            speak("No result found!")
                    elif "no" in X:
                        print("Ok")
                        speak("Ok")
                

elif ip==2:
    if __name__ == "__main__":
        while True:
            query = takeCommand().lower()

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

            elif 'who are you' in query:
                speak("I am a basic AI Technology based prototype named Gideon sir...")
                print("I am a basic AI Technology based prototype named Gideon sir...")

            elif 'your name' in query:
                speak("My name is Gideon.")
                print("My name is Gideon.")

            elif 'you have feelings' in query:
                speak("Yes sir, I have lots of emotions. I feel excited when I learn something new.")
                print("Yes sir, I have lots of emotions. I feel excited when I learn something new.")

            elif 'you like me' in query:
                speak("I like you even more than anything else sir..." )
                print("I like you even more than anything else sir..." )

            else:
                try:
                    res = app.query(query)
                    print(next(res.results).text)
                    speak(next(res.results).text)
                except:
                    gsearch = takeCommand().lower()
                    pywhatkit.search(f"{gsearch}")