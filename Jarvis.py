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
import pathlib
from dotenv import load_dotenv
from googlesearch import search
import time 
import os.path
from os import path
import openai


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[2].id)
print(voices)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

load_dotenv()

EMAIL = os.getenv('EMAIL')
PASS = os.getenv('PASS')
PERSON1 = os.getenv('PERSON1')
PERSON2 = os.getenv('PERSON2')
GPT = os.getenv("GPT")
USERNAME = os.getenv("USERNAME")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    #speak("I am Jarvis your virtual assistant . How may I help You")       

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
        #speak("Sorry I did not get thet") 
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(EMAIL, PASS)
    server.sendmail(EMAIL, to, content)
    server.close()

def askGPT(text):
    openai.api_key = GPT
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        temperature = 0.6,
        max_tokens = 100,
    )
    return speak(response.choices[0].text)
    #return print(response.choices[0].text)




if __name__ == "__main__":
    #wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'jarvis' in query:
            
            query = query.replace('jarvis', '')
            # Logic for executing tasks based on query
            if 'search wikipedia for' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "").strip().lower()
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
            elif 'ask gpt ' in query or 'asked gpt' in query:
                    query = query.replace('ask gpt ', "").strip().lower()
                    askGPT(query)
                    print('\n')
            elif 'open ' in query :
                query = query.replace('open ','').strip().lower()
                print(query)
                if query == 'youtube':
                    webbrowser.open_new_tab("http://www.youtube.com")
                elif query == 'google':
                    webbrowser.open_new_tab("http://www.google.com")
                elif query == 'terraria':
                    terrariaPath = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Terraria.exe"
                    os.startfile(terrariaPath)
                elif query == 'discord':
                    discordPath = "C:\\Users\\USERNAME\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk" 
                    os.startfile(discordPath)
                elif query == 'steam':
                    steamPath = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Steam\\Steam.lnk'
                    os.startfile(steamPath)
                elif query == 'bluestacks':
                    bluestacksPath = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\BlueStacks5.lnk'
                    os.startfile(bluestacksPath)
                    time.sleep(2)
                    keyboard.press('Enter')
                elif query == 'epicgames':
                    epicgamesPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Epic Games Launcher.lnk"
                    os.startfile(epicgamesPath)
                elif query == 'chess':
                    webbrowser.open_new_tab('http://www.chess.com')
                elif query == 'vs code':
                    codePath = "C:\\Users\\USERNAME\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
                    os.startfile(codePath)
                elif query == 'obs':
                    codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Streamlabs Desktop.lnk"
                    os.startfile(codePath)
                else:
                    webbrowser.open_new_tab(query)
            elif 'wish me' in query:
                wishMe()    
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")
            elif 'play music' in query:
                music_dir = 'C:\\Users\\Praveen verma\\Music\\My Songs'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))
            elif 'type' in query:
                speak('Typing...')
                speak("What should I Type?")
                command = takeCommand()
                print(command)
                keyboard.write(command,delay=0.35)
                if 'enter' or "Enter" in command:
                    keyboard.press('Enter')
                if "backspace" or "Backspace" in command:
                    keyboard.press('Backspace') 
            elif 'shutdown' in query or "shut down" in query:
                speak("are you sure sir? this command will shutdown the entire system.")
                command = takeCommand()
                if 'yes' in command:
                    os.system("shutdown /s /t 1")
                else:
                    speak("Command aborted")
            elif 'restart' in query:
                speak("Are you sure sir? This command will restart this system.")
                command = takeCommand()
                if 'yes' in command:
                    os.system("shutdown /r /t 1")
                else:
                    speak("Command aborted")
            elif 'log out' in query or 'logout' in query:
                speak("Are you sure sir? This command will log you out of the system")
                command = takeCommand()
                if 'yes' in command:
                    os.system("shutdown /l")
                else:
                    speak("Command aborted")
            elif 'email to mom' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = PERSON1    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry I am unable send this email")   
            elif 'email to dad' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = PERSON2    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry I am unable send this email") 
            elif 'email to myself' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = EMAIL    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry I am unable send this email")
    
