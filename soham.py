import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
import requests
from bs4 import BeautifulSoup
import sys
import time
import pyjokes
import cv2
import weathercom
import json
           
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#print(voices)

def speak(audio):
    engine.say(audio)
    engine.runAndWait() 

# TO Wish 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%H:%p")

    if hour >=0 and hour <=12:
        speak(f"Good morning sir,")
    elif hour >=12 and hour<=18:
        speak(f"Good afternoon sir,")            
    else:
        speak(f"Good evening sir,")       

def date():
    date = int(datetime.datetime.now().day)
    speak(date)

def month():
    speak("december")

def year():
    #year = int(datetime.datetime.now().year)
    speak("two thousand twenty")    

def times():
    lop = datetime.datetime.now().strftime("%I:%M:%S")
    speak(lop)    

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        speak("Say that again please...")
        return "None"
    return query  

def sendEmail(to,content):
    server =  smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("navalesoham12@gmail", "soham@9205")
    server.sendmail("navalesoham12@gmail.com", to, content)
    server.close()       
    
    
if __name__ =="__main__":
    wishMe()
    speak("hello")
    speak("i am jarvis")
    speak("your personal assistant")
    speak("Loading and updating your today's package")
    speak('done')
    speak('welcome sir')
    speak('first of all i will give you todays information')
    speak("your current location is in ,  sangola city")
    speak("Current time is")
    speak(times())
    speak("Today's date is")
    speak(date())
    speak("Current month is")
    speak(month())
    speak("Current year is")
    speak(year())
    speak("sir your home temperature is 25 degree celcius")
    speak("weather outside is clear with partly cloudy")
    speak("temperature outside is 23 degree celcius")
    speak("humidity outside is 33 percent")
    speak("wind speed outside is 7 kilometre per hour")
    #speak("today you have 3 projects regarding to coding")
    #speak("first is of  weather mapping")
    #speak("and second is of , chat bot making")
    #speak("and third is of , tracking location bot")
    speak(" , sir there are zero devices connected to your wifi")
    speak("please tell me now that how can i help you?")
    while True:
        query = takecommand().lower()

        if 'according to wikipedia' in query:
            speak("Searching on wikipedia")
            query = query.replace('according to wikipedia','')
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open notepad' in query:
            speak("opening notepad")
            npath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(npath)  

        elif 'open google' in query:
            speak("opening google")
            apath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(apath)

        elif 'name' in query:
            speak('My name is jarvis')     

        elif 'yourself' in query:
            speak('I am a voice assistant designed by soham')

        elif 'open cmd' in query:
            speak("opening cmd")
            os.system('start cmd') 

        elif 'open camera' in query:
            speak("opening camera sir")
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()       

        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f'your ip address is {ip}')

        elif 'play music' in query:
            music_dir = "C:\\Users\\Soham Navale\\Desktop\\songs"   
            songs = os.listdir(music_dir)
            #rd = random.choice(songs)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif 'open youtube' in query:
            speak("opening youtube sir")
            webbrowser.open("www.youtube.com")

        elif 'weather in pune' in query:
            speak("sir getting weather information of pune")
            speak("Sir weather in pune is mostly cloudy")
            speak("temperature in pune is 23 degree celcius")
            speak("humidity in pune is 5 percent")
            speak("wind speed is 1 kilometre per hour")

        elif 'weather in mumbai' in query:
            speak("sir getting weather information of mumbai")
            speak("Sir weather in mumbai is smoke cloud")
            speak("temperature in mumbai is 31 degree celcius")
            speak("humidity in mumbai is 59 percent")
            speak("wind speed is 11 kilometre per hour")

        elif 'weather in solapur' in query:
            speak("sir getting weather information of solapur")
            speak("Sir weather in solapur is clear with periodic clouds")
            speak("temperature in solapur is 27 degree celcius")
            speak("humidity in solapur is 51 percent")
            speak("wind speed is 2 kilometre per hour")

        elif 'weather in delhi' in query:
            speak("sir getting weather information of delhi")
            speak(" , weather in delhi is smoke cloud")
            speak(" ,temperature in delhi is 25 degree celcius")
            speak(" ,humidity in delhi is 43 percent")
            speak(" ,wind speed is 1 kilometre per hour")        

        elif 'open github' in query:
            speak("opening github sir")
            webbrowser.open("www.github.com")

        elif 'open facebook' in query:
            speak("opening facebook sir ")
            webbrowser.open("www.facebook.com")

        elif 'open instagram' in query:
            speak("opening instagram sir")
            webbrowser.open("www.instagram.com")

        elif 'open gmail' in query:
            speak("opening gmail sir")
            webbrowser.open("www.gmail.com")

        elif 'my bitcoin balance' in query:
            speak('your bitcoin balance is 64 dollar')  

        elif 'what is my yesterday bitcoin balance' in query:
            speak('your yesterdays bitcoin balance was 49 dollar')

        elif "google is perfect" in query:
            speak("yes , google is perfect than me because it is has more functions and more specification")
            speak("but i can try to get me more updating by which i can defeat google")
            speak("because a person said that work hard , you will definitely get success")

        elif "your friends" in query:
            speak("my friends are alexa , google and siri")

        elif "my family" in query:
            speak("your father's name is somnath navale")
            speak("your mother's name is manisha navale")
            speak("your sister's name is mansi navale")       

        elif 'will you marry me' in query:
            speak('sorry sir , i cant marry you , but i can help you as an assistant to solve your problems')                  

        elif 'search on google' in query:
            speak('sir, what should i search on google')
            cm = takecommand().lower()
            speak("ok sir , searching on google")
            webbrowser.open(f'{cm}') 

        elif 'send whatsapp message' in query:
            kit.sendwhatmsg('+917875719502', 'this is testing protocol',4,13)
            time.sleep(120)
            speak('message has been sent')

        elif "netflix account" in query:
            speak("getting information of your netflix account")
            speak("your email is soham navale ,  at the rate gmail dot com")   
            speak("your password is soham at the rate 0 2 2 0")
            speak("getting information of your subscription")
            speak("your subscription will end on 16 november two thousand twenty")

        elif "my telegram id" in query:
            speak("your telegram id is , at the rate soham navale")  

        elif "who is your boss" in query:
            speak("my boss name is soham navale")      

        elif "can you help" in query:
            speak("i can help you in anything but my maths is weak so i cant help you in maths problems")     

        elif 'song on youtube' in query:
            speak("playing song youtube sir")
            kit.playonyt('see you again')

        elif 'ipl score' in query:
            speak("opening on browser") 
            score = 'ipl 2020'
            webbrowser.open(f'{score}')

        elif 'owner of microsoft' in query:
            speak("sir owner of microsoft is bill gates") 

        elif 'owner of amazon' in query:
            speak("sir owner of amazon is jeff bezos")  

        elif 'owner of google' in query:
            speak("sir google has no personal owner but it has a parent organiztion owner named alphabet inc")         


        elif 'who is my brother' in query:
            speak('Your brother is raahul and paarth ')    

        elif "who am i" in query:
            speak("you are my sir named soham navale who created me")    

        elif 'send email' in query:
            try:
                speak('what should i say?')
                content = takecommand().lower()
                to = "sohamnavale15@gmail.com"                 
                sendEmail(to,content)
                speak('email has been sent to email') 

            except Exception as e:
                print(e)
                speak('sorry sir, i am not able to send this mail to mansi')

        elif 'you can sleep' in query:
            speak('thanks for using me sir,  have a good day.')
            sys.exit()
# Weather Coding
        elif "weather in" in query:
            speak('Temprature in ekhatpur is  30 degree celcius  and humidity in ekhatpur is moderate  and weather description  in ekhatpur is slow rain ')
           
           
# To Close Application 
        elif 'close notepad' in query:
            speak('okay sir, closing notepad')
            os.system('taskkill /f /im notepad.exe')

        elif 'close google' in query:
            speak('okay sir, closing google')
            os.system('taskkill /f /im chrome.exe')   
# Set An Alaram
        elif 'set alarm' in query:
            nn = int(datetime.datetime.now().hour)
            if nn==22:
                music_dir = "C:\\Users\\Soham Navale\\Desktop\\songs"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
# To Tell Me Joke 
        elif 'tell me a joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'shut down the system' in query:
            os.system('shutdown /s /t S')

        elif 'restart the system' in query:
            os.system('shutdown /r /t S') 

        elif 'sleep the system' in query:
            os.system('rundll32.exe powrproof.dll,SetSuspend 0,1,0') 

        
