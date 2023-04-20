import time
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os
import pyjokes
from userinfo import *
from sys_dir_files import *
from jarvis_func import *
from jarvis_openai import Jarvis_keys
import naukri_apply_bot
import os




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def jarvis(speak):
    engine.say(speak)
    engine.runAndWait()

def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        jarvis("Good Morning!")
        return False

    elif hour>=12 and hour<18:
        jarvis("Good Afternoon!")  
        return False 

    else:
        jarvis("Good Evening!") 
        return True



def takeorder():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('started.. you can speak now..')
        r.adjust_for_ambient_noise(source,duration=2)
        r.pause_threshold = 1.5
        rec_order = r.listen(source)
        try:
            print("recognizing ur order....")
            order = r.recognize_google(rec_order)
            order = order.lower()
            if 'take order' in order and 'how' not in order:
                take_order = input('Enter your order: \n')
                return take_order
            elif 'jarvis' in order:
                order = order.replace('jarvis','')
                print(order)
                return order
            else:
                print(order)
                return order
            
        except Exception as e:
            print('something went wrong! say it again')
            return 'None'
 
def whatsappmessage_timer():
    now = datetime.datetime.now()
    hr = now.strftime("%H")
    mini =now.strftime("%M")
    t_min= mini
    t_min = int(t_min)+2
    li = [hr,t_min]
    return li
 
        
        
    
    
        
if __name__=="__main__" :
    greeting()
    jarvisfunc()
    jarvis("tell me how may I help you")
    conversation = ''
    while True:
        order = takeorder()
        if order == 'None':
            takeorder()


        if 'wikipedia' in order:
            jarvis('searching wikipedia')
            results = wikipedia.summary(order, sentences=2)
            jarvis('According to wikipedia')
            jarvis(results)
        elif 'play' in order and 'youtube' in order:
            jarvis('opening youtube')
            pywhatkit.playonyt(order)
        elif 'open google' in order:
            jarvis('opening google chrome')
            webbrowser.open(google)
        elif 'open youtube' in order:
            jarvis('opening youtube')
            webbrowser.open('https://www.youtube.com')
        elif 'apply job' in order or 'start naukri bot' in order or 'start naukri bot' in order :
            jarvis('starting apply flutter jobs')
            # naukri_flutter_bot()
            jarvis('starting apply python jobs')
            # naukri_python_bot()
            jarvis('finished applying jobs')
        elif 'open github' in order:
            jarvis('opening github')
            webbrowser.open(githubacct)
        elif 'open gmail' in order or 'open mail' in order:
            jarvis('opening gmail')
            webbrowser.open(gmail)
        elif 'open google chrome' in order or 'open chrome' in order:
            jarvis('opening google chrome')
            webbrowser.open(google)
        elif 'open spotify' in order:
            jarvis('opening spotify')
            os.startfile(spotify)
        elif 'play some music' in order or 'play music' in order or 'play song' in order:
            jarvis('opening music')
            webbrowser.open(spotifyweb)
        elif 'open code editor' in order or 'open vs code' in order or 'open visual studio' in order:
            jarvis('opening code editior')
            os.startfile(vscode)
        elif 'whatsapp' in order or 'send message in whatsapp' in order or 'message in whatsapp' in order:
            jarvis('ok whom to send message')
            person = takeorder()
            if person == 'None' or person == ' ' or person == '' or person==None:
                jarvis("say again. whom to send message")
                person = takeorder()
            
            person = person.replace(" ","")
            if person in contact:
                number = contact[person]
                jarvis('whats message')
                message = takeorder()
            else:
                jarvis(person+' number')
                number = takeorder()
                number = '+91'+number
                number = number.replace(" ","")
                jarvis('whats message')
                message = takeorder()
            timer = whatsappmessage_timer()    
            print(f'number = {number}, message = {message}')
            pywhatkit.sendwhatmsg(number,message,int(timer[0]),int(timer[1]))
            jarvis('message sent successfully')
        elif 'time now' in order or 'whats time' in order or 'time' in order:
            now = datetime.datetime.now().strftime("%I:%M %p")
            print(now)
            jarvis(now)
        # elif 'what is' in order or 'search what is' in order or 'search what are' in order or 'what are' in order or 'is that' in order or 'search' in order or 'find' in order:
        #     jarvis('searching')
        #     print(order)
        #     pywhatkit.search(order)
        elif 'create a folder' in order or 'create folder' in order:
            jarvis('folder name')
            dic_name  = takeorder()
            dic_name = dic_name.replace(" ","")
            parentdic = "C:/Users/syedsyed/Desktop"
            path = os.path.join(parentdic, dic_name)
            print(path)
            os.mkdir(path)
            jarvis('created successfully')
        elif 'joke' in order:
            jarvis(pyjokes.get_joke())
        elif 'shutdown' in order and 'system' in order:
            os.system("shutdown /s /t 1")
        elif 'close google window' in order or 'close chrome' in order or 'close chrome window' in order:
            os.system("taskkill /im chrome.exe /f")
        elif 'close work tabs' in order or 'close window tabs' in order or 'close all tabs' in order:
            os.system("taskkill /im chrome.exe /f")
            os.system("taskkill /im Code.exe /f")
            os.system('taskkill /im chrome.exe')
# os.system('taskkill /im POWERPNT.exe')
# os.system('taskkill /im OUTLOOK.exe')
# os.system('taskkill /im WINWORD.exe')
# os.system('taskkill /im ArcMap.exe')
# os.system('taskkill /im acadlt.exe')
# os.system('taskkill /im EXCEL.exe')
# os.system('taskkill /im AcroBat.exe')
# os.system('taskkill /im wmplayer.exe')

        elif 'set timer' in order :
            jarvis('for how many minutes')
            minutes_timer = takeorder()
            if minutes_timer!='':
                created_timer_command = 'timer is set for '+minutes_timer
                jarvis(created_timer_command)
        elif 'set alarm' in order :
            jarvis('alarm Time')
            alarm_timer = takeorder()
            if alarm_timer!='':
                created_alarm_command = 'alarm is set for '+alarm_timer
                jarvis(created_alarm_command)
         
        elif 'start naukri' in order:
            jarvis('Starting applying Naukri jobs')
            naukri_apply_bot.naukri_flutter_bot()
            jarvis('flutter task is finished')
            naukri_apply_bot.naukri_python_bot()
            jarvis('python task is finished')
            time.sleep(2)
            jarvis('applying task is finished')
        else:
            if order!='None':
                prompt = name + ":" + order + "\n" + Jarvis_keys.Bot_name + ":"
                conversation += prompt
                response = Jarvis_keys.jarvis_operation(prompt)
                conversation += response + "\n"
                print(response)
                jarvis(response)
                
            
                
                
