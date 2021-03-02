import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser#pip install webbrowser
import os
import pyautogui#pip install pyautogui
import smtplib
import keyboard
import site
from googlesearch import search
from time import sleep

Email = #put ur email here
Pass = #put ur password here
Coumputer_name = #put you coumputer name here
Dad = #put your dad's email here
Mom = #put your Mom's email here

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis your virtual assistant . How may I help You")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e: 
        print(e)    
        print("I diden't get that") 
        speak("Sorry I did not get thet") 
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(Email, Pass)
    server.sendmail(Email, to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'search wikipedia for' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=10)
                speak("According to wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print('sorry no such results found')
                speak('sorry no such results found')
        elif 'pause' in query:
            speak('Paused')
            os.system("pause")
        elif 'quit' in query:
            speak('Quitting')
            os._exit(0) 
        elif 'open ' in query :
            name = query.replace('open ', '')
            if name == 'youtube':
                webbrowser.open_new_tab("http://www.youtube.com")
            elif name == 'google':
                webbrowser.open_new_tab("http://www.google.com")
            elif name == 'terraria':
                steamPath = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Terraria.exe"
                os.startfile(steamPath)
            elif name == 'discord':
                discordPath = "C:\\Users\\"+Computer_name+"\\AppData\\Local\\Discord\\Update.exe" 
                os.startfile(discordPath)
            else:
                webbrowser.open_new_tab(name)
        elif 'wish me' in query:
            wishMe()    
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")        
        elif 'open code' in query:
            codePath = "C:Users\\"+Computer_name+"\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'obs' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Streamlabs OBS.lnk"
            os.startfile(codePath)
        elif 'steam' in query:
            steamPath = "C:\\Users\\"+Computer_name+"\\Desktop\\Steam.lnk"
            os.startfile(steamPath)
        elif 'wikipedia' in query:
            webbrowser.open_new_tab("https://en.wikipedia.org/wiki/Wiki")
        elif 'email to mom' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = Mom    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am unable send this email")   
        elif 'email to dad' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = Dad    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am unable send this email") 
        elif 'email to myself':
            try:
                speak("What should I say?")
                content = takeCommand()
                to = Email    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I am unable send this email")
