import speech_recognition as sr
import requests
import pyttsx3

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_info_from_internet(query):
    try:
        response = requests.get(f'https://api.duckduckgo.com/?q={query}&format=json')
        data = response.json()
        return data['AbstractText'] if data['AbstractText'] else "Sorry, I couldn't find any information on that topic."
    except Exception as e:
        return str(e)

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Please say something")
    audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        speak(f"You said: {text}")
        
        # Fetch information based on the recognized text
        info = get_info_from_internet(text)
        print(info)
        speak(info)
        
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        speak("Sorry, I did not understand that.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        speak(f"Could not request results; {e}")
