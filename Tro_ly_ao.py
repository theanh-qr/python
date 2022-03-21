import speech_recognition
import pyttsx3
from datetime import date
from datetime import datetime


while True:
    robot_ear = speech_recognition.Recognizer()
    robot_mouth = pyttsx3.init()
    robot_brain = ""

with speech_recognition.Microphone() as mic:
    print("Robot:  I'm Listening")
    audio = robot_ear.Listen(mic)

    print("Robot: ...")

try:
    you = robot_ear.recognize_google(audio)
except:
    you = ""
    print("You:" + you)

if you == "":
    robot_brain = "I can't hear you,try again"
elif you == "hello":
    robot_brain = "Hello The Anh"
elif "today" in you:
    today = date.today()
    robot_brain = today.strftime("%B %d, %Y")
elif "time" in you:
    today = date.now()
    robot_brain = today.strftime("%H hours %M minutes  %S seconds")
elif "name you" in you:
    robot_brain = "My name is Robot"
elif you == "Bye":
    robot_brain = "Bye The Anh"
    print("Robot:" + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
    break
else:
    robot_brain = "I'm fine thank you"

    
print("Robot:" + robot_brain)
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()
