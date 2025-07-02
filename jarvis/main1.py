import speech_recognition as sr # Importing the speech recognition module
import webbrowser # Importing the webbrowser module to open URLs
import pyttsx3 # Importing the text-to-speech engine
import musiclibrary # Importing the music library
import requests # Importing requests for API calls
import google.generativeai as genai # Importing Google Generative AI for advanced features
from gtts import gTTS # Importing Google Text-to-Speech for text-to-speech conversion   
import pygame # Importing pygame for audio playback
import os # Importing os for file operations


#pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "" #add your newsapi key value
def speak_old(text):
    engine.say(text)
    engine.runAndWait()   

def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

# Wait until playback finishes
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")  # Clean up the temporary file after playback

    


def aiProcess(command):
    genai.configure(api_key="")  # Replace with your actual API key
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(command)
    print(response.text)
    speak(output=response.text)


def processCommand(c):

    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com") 
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # If the request was successful, parse the JSON response
            data = r.json()
            if data["status"] == "ok":
                print("Top IN Headlines:\n")
                for i, article in enumerate(data["articles"]):
                    speak(f"{i+1}. {article['title']}")
                else:
                    speak("Sorry, I couldn't fetch the news right now.")
    #gemini handle the request
    else:
        output = aiProcess(c)
        speak(output)




if __name__=="__main__":
    speak("Initializing Jarvis.....")
    while True:
    #Listen for the word "jarvis"
    # obtain audio from the microphone
        r = sr.Recognizer()


        print("Recognizing...")
        # recognize speech using Google Speech Recognition
        # If you want to use a different recognizer, you can replace `recognizer`
        try:
            with sr.Microphone() as source:
                print("Say something!")
                audio =r.listen(source, timeout=10, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Ya")
                with sr.Microphone() as source:
                    print("Jarvis Active")
                    audio = r.listen(source)
                    command=r.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print("Jarvis error:",e)