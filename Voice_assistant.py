import speech_recognition as sr # speech to text
import pyttsx3 # text to speech
import playsound # to play mp3 files
import webbrowser # to open url in default browser
import pywhatkit # to automate whatsapp
import wikipedia # to get results from wikipedia
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio): # get audio as text
    engine.say(audio)
    engine.runAndWait()
# get audio from the microphone
def micro(): #get audio from user
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=2)
        print("Speak:")
        audio = r.listen(source)
        rec=r.recognize_google(audio)
        return rec.lower()
def wake(): # to play sound
    playsound.playsound('C:\\Users\\ADMIN\\Downloads\\when.mp3')
    try:
        while(1<2):
            micinput = micro()
            if 'what is your name' in micinput:
                wake()
                print("my name is jarvis a voice assistant")
                speak('my name is jarvis a voice assistant')
            if 'hello jarvis' in micinput:
                wake()
                speak('hello sir')
            if 'bye' in micinput:
                wake()
                print("thank you sir have a nice day")
                speak("thank you sir have a nice day")
                exit()
            if 'open google' in micinput:
                wake()
                speak("opening google")
                webbrowser.open("www.google.com")
            if 'message albert' in micinput:
                wake()
                speak("sending message")
                pywhatkit.sendwhatmsg("+919677360426", "Hi albert!!", 12, 23)
            if 'wikipedia' in micinput:
                wake()
                speak(f"getting results for {micinput.replace('wikipedia','')}")
                print(wikipedia.summary(micinput.replace("wikipedia",""),sentences=5 ))
                speak(wikipedia.summary(micinput.replace("wikipedia",""),sentences=5))
            if 'addition' in micinput:
                wake()
                speak('enter numbers')
                list1 = list(map(int,input('Enter Numbers').split()))
                print(f"sum={sum(list1)}")
                speak(f"sum equals {sum(list1)}")
            else:
                print(f'you said {micinput}')
                speak(f'you said {micinput}')
    except :
        print("Could not understand audio")