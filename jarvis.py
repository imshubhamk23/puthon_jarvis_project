import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("Good Morning Sir!")

    elif hour > 12 and hour < 18:
        speak("Good Afternoon Sir!!")

    else:
        speak("Good Evening Sir!")

    speak("I am Jarvis, Please tell me how may I help you?") 

def takecommand():
    '''
    It takes microphone input from user and returns string output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language="en-in")
        print(f'User said: {query}\n')
    
    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()
        #logic for executing task based on query
        if "wikipedia" in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open google" in query:
            webbrowser.open("www.google.com")

        elif "open stack overflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "play music" in query:
            music_dir = "D:\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            num = random.randrange(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[num]))

        elif "exit" in query or "stop" in query or "end" in query or "goodbye" in query:
            speak("Goodbye Sir!")
            exit()

        elif "hello" in query or "hi" in query:
            speak("Hello Sir!")

        elif "next song" in query:
            music_dir = "D:\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            num = random.randrange(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[num]))