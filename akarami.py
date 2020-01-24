import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[10].id)
engine.setProperty('voice',voices[10].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning sir!')
    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    else:
        speak('Good evening')
        
    speak('hello I am akarami how may i help you')   


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold = 1
        r.energy_threshold = 300
    
        audio = r.listen(source)

    try :
        print('recognoing...')
        query = r.recognize_google(audio, language='en-in')
        print('user said:{query}\n')

    except Exception as e:
         print('say that again please.....')
         return "None"    
    return query     





if __name__=='__main__':
   wishMe()
   while True :
       query = takeCommand()
       #logic for execution
       if 'wikipedia' in query:
           speak('Searching Wikipedia...')
           query = query.replace('wikipedia','')
           results = wikipedia.summary(query,sentences = 2)
           speak('accourding to wikipedia')
           speak(results)
           
           
       elif 'open youtube' in query:
          webbrowser.open('youtube.com')   
