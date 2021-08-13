import datetime
import os
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning!")

    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Zira. Please tell me how may I help you")


def takeCommand():
    #takes microphone input from the user and returns string output

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
        print("Say that again please...")
        return "None"
    return query


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('my@gmail.com', 'C:\\Users\\ARFA FATHIMA\\Desktop\\est\pass.txt')
    server.sendmail('my@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    wishme()
    while True:
     #if 1:
        query = takeCommand().lower()

        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Ma'am the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1.3\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'send email to arfa' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "arfaaa.fathima@gmail.com"
                sendemail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")
