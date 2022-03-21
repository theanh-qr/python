import speech_recognition

robot_eat = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
	print("Robot: I'm listening")
	audio = robot_ear.listen(mic)
you = robot_ear.recognize(audio)
print(you)