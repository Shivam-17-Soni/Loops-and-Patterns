import datetime
import webbrowser
import os
import smtplib
# Above are in built modules or libraries. Below are that we have to install using pip.
import pyttsx3                       # install pyttsx3 module
import speech_recognition as sr      # intall speechRecognition module and PyAudio And pipwin library
import wikipedia                     # install wikipedia module


engine = pyttsx3.init('sapi5')          # "sapi5" is API provided by windows to take voice input.
voices = engine.getProperty('voices')
# Voices in computer
# print(voices)
# print(voices[0].id)  # male voice
# print(voices[1].id)  # female voice
# print(voices[2].id)  # female voice
engine.setProperty('voice',voices[1].id)

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
    
    speak("Hello Dear, I am your friend. Please tell me how may I help you.")


def takeCommand():
    # It takes microphone input from the user and returns string output.

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")  # To show that, AI is listening.
        r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete. So, if we pause for a second it doesnot take it as complete command.
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        #print(e)   # To print error.
        print("Say that again please...")
        return "None" # Returning 'None' if a error or problem occurs.
    return query 
    # This function is taking audio as input and returning it as string.

def sendEmail(to,content):
    # We have to allow less secured appps in gmail to send mails.
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your email password')      # It is better to take it from the text file.
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    # Logic for executing tasks based on query.
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            #print(results)
            speak(results)
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            # music_dir =       # path of folder in pc
            # songs = os.listdir(music_dir)
            # print(songs)
            # os.startfile(os.path.join(music_dir,song[0]))     # Plays 1st song. We can use random module to listen random song each time we use this command.
            webbrowser.open('ganna.com')
        
        elif 'the time' in query:
            strTime =datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mitra, The time is {strTime}")
        
        elif 'open vs code' in query:
            vsCodePath = "C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vsCodePath)
        
        elif 'email to shiv' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "shivasoni123456789@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                # print(e)
                speak("Sorry my dear. I am not able to send this mail.")
        
        elif 'quit' in query:
            exit()

# Challange add more functionalities in it.