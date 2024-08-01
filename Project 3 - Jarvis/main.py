import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI 
from gtts import gTTS
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "Your API Key"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 

def aiprocess(command):

    client = OpenAI(
    api_key="Open Ai API Key",
    )

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please "},
        {"role": "user", "content": command}
    ]
    )

    return(completion.choices[0].message.content)


def processCommand(c):
    if "open google" in c.lower():
        print("Opening Google")
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        print("Opening Facebook")
        webbrowser.open("https://facebook.com")

    elif "open linkedin" in c.lower():
        print("Opening Linkedin")
        webbrowser.open("https://linkedin.com")

    elif "open instagram" in c.lower():
        print("Opening Instagram")
        webbrowser.open("https://instagram.com")

    elif "open youtube" in c.lower():
        print("Opening Youtube")
        webbrowser.open("https://youtube.com")

    elif c.lower().startswith("play"):
        print("Playing Songs")
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        print("Playing News")
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
    else:
        # let OpenAI handle the request
        output = aiprocess(c)
        speak(output)

if __name__ == "__main__":
    speak("Welcome Hy I am jarvis: ")

    while True:
        
        # Listen for wake up word jarvis
        # obtain audio from the microphone
        
        r = sr.Recognizer()

        print("Recognizing..")
        try:
            with sr.Microphone() as source:
                print("listening..")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)

            if(word.lower() == "jarvis"):
                speak("How can I help you")

                # Listen for command 
                with sr.Microphone() as source:
                    print("Jarvis Active..")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error;{0}".format(e))