from datetime import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia

engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)



def speak(audio):
    """
    This Funcation speaks every thing that is given as an argument. You can call this funtion manually or use a loop as per the situation
    """

    engine.say(audio)
    engine.runAndWait()


def wishme():
    """
    This function wishes you as per the time of the day, For ex:- If it is Afternoon which is between 12pm to 5pm then this program will wish you 'Good Afternoon'. This function uses the module name Datetime to extract the time.
    """


    hour = int(datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<17:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
    
    speak("I'm wikipedia article extractor, tell me which article to fetch")



def takecommand():
    """
    This function takes voice input and converts it into text, Then that text is used to extract the article from Wikipedia. This uses google speech to text program.
    """
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    
    except Exception:
        print("Can you say that again please")
        return "None"
    

    return query

if __name__ == '__main__':
    wishme()
    while True:

        query = takecommand().lower()

        if query == 'exit':
            speak("Have a good day!")
            break

        speak("Searching Wikipedia...")
        results = wikipedia.summary(query, sentences = 2)
        speak("According to wikipedia")
        print(results)
        speak(results)




