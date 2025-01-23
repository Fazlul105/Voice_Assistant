import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return ""

def main():
    speak("Hello! I am pushpa jookaiga nehi sala ")
    while True:
        command = listen()
        if "hello" in command:
            speak("Hello! How can I help?")
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}.")
        elif "search for" in command:
            query = command.replace("search for", "").strip()
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching for {query}.")
        elif "exit" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()

