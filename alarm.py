import pyttsx3
import datetime
import csv
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

now = datetime.datetime.now()
current_time = now.strftime("%H:%M")

try:

    file = open("Remind.csv",'r')
    speak("What do you want to be remind?")
    work_input = input("What do you want to be remind? ")
    read = csv.reader(file)

    def reminder(remind):
        for val in read:
            if current_time == val[0]:
                speak(remind)
                if work_input in "open youtube":
                    webbrowser.open("https://www.youtube.com/")
                elif work_input in "open google":
                    webbrowser.open("https://www.google.com")
            else:
                speak("you have much time in your reminder.")
    reminder(work_input)

except:
    pass