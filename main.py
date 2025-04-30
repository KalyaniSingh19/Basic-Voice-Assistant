import subprocess
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good morning')
    elif hour >= 12 and hour < 18:
        speak('Good afternoon')
    else:
        speak('Good evening')

    assname = 'Clara'
    speak('I am your virtual assistant')
    speak(assname)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')
        return query
    except Exception as e:
        print('Unable to understand. Please say that again...')
        return None

def user():
    speak('What is your name?')
    uname = None
    while uname is None:
        uname = takeCommand()
    speak(f"Hi {uname}")
    print(f"User name: {uname}")
    speak('Okay, how can I help you?')

if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    wish()
    user()

    while True:
        query = takeCommand()
        if query is None:
            continue

        query = query.lower().strip()

        if 'wikipedia' in query:
            speak('Okay, searching Wikipedia...')
            try:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except Exception as e:
                speak("Sorry, I couldn't find any results.")
        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif "play music" in query:
            speak("Opening Spotify")
            try:
                subprocess.Popen("start Spotify", shell=True)
            except Exception:
                speak("Couldn't open Spotify")
        elif "time" in query:
            ttime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {ttime}")
        elif "exit" in query:
            speak("Bye bye for now")
            break
