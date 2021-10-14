import pyttsx3 #
import datetime #
import speech_recognition as sr #
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5') #
voices = engine.getProperty('voices')
# print(voices[0].id)
# print(voices[1].id) 
engine.setProperty('voices',voices[1].id) #


def speak(audio):
    engine.say(audio)
    engine.runAndWait() #


def wishme():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am Jarvis, your personal AI assistant. How may I help you sir ?")

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("adarshraj3309@gmail.com","9826781397")
    server.sendmail("adarshraj3309@gmail.com",to,content)
    server.close()
    
def takecommand():
    r = sr.Recognizer() #
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5 
        audio = r.listen(source)
        
    try:
        print("Recognising...")
        query = r.recognize_google(audio,language = 'en-in') #
        print(f"User said {query}")
    except Exception as e:
        # print(e)
        
        speak("Please say that again...")
        return "None"
    return query
        

if __name__ == "__main__":
    # speak("shut up")
    # takecommand()
    wishme() 
    while True:
        query = takecommand().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            # print(results)
            speak("According to wikipedia"+ results)
            
        if "open youtube" in query:
            webbrowser.open("www.youtube.com")
            
        if "open google" in query:
            webbrowser.open("www.google.com")
            
        if "open gfg" in query:
            webbrowser.open("www.geeksforgeeks.com")
            
        if "open stackoverflow" in query:
            webbrowser.open("www.stackoverflow.com")
            
        if "let's practice some cp" in query:
            webbrowser.open("www.codechef.com")
            
        if "play music" in query:
            music_dir = "D:\\Programming\\PYTHON\\JARVIS"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
            
        if "the time" in query:
            strTime =  datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")
        
        if "open code" in query:
            codePath = "C:\\Users\\Adarsh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        if "send email to yuvraj" in query:
            try:
                speak("What should I  say ?")
                content = takecommand()
                to = "yuvrajrte047@sicaschool54.org"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("I am not able to send the mail, sorry for the inconvenience")
        
        
        if "and exit" in query:
            exit(1)