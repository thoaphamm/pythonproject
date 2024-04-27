import speech_recognition as sr  
from speech_recognition import WaitTimeoutError
from gtts import gTTS  
import os 
import pyttsx3
from datetime import date 
from datetime import datetime 

r=sr.Recognizer()
robot_ear = sr.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""
def listen():
     robot_ear = sr.Recognizer() 
     with sr.Microphone() as source:
         print("Robot:...")

     try:
         robot_ear.adjust_for_ambient_noise(source, duration=1)
         audio_data = robot_ear.listen(source, timeout=5)
         text = robot_ear.recognize_google(audio_data)
         print("Robot:...")
def speak():
     tts = gTTS(you=you,lang='vi')
     filename='voice.mp3'
     tts.save(filename)
     playsound.playsound(filename)
     os.remove(filename)
while True:
     with sr.Microphone() as source:
         print("Robot: Em nghe đây ạ")
         robot_ear.adjust_for_ambient_noise(source)
         audio_data = robot_ear.listen(source,timeout=5)
     print("Robot:...")

     try:
         you = robot_ear.recognize_google(audio_data,language="vi")
     except:
        you = ""

     print("You: " +you)

     if you == "":
         robot_brain = "Em đây ạ "
     elif "xin chào" in you:
         robot_brain = "xin chào Thoa"
         print(robot_brain)
         speak(robot_brain)
     elif "ngày" in you:
         today = date.today()
         robot_brain = today.strftime("%d/%m/%Y") 
         print(robot_brain)
         speak(robot_brain)
     elif "giờ" in you:
         now = datetime.now()
         robot_brain = now.strftime( "%H:%M:%S")
         print(robot_brain)
         speak(robot_brain)
     elif "tổng thống" in you:
         robot_brain = "Pham Thi Thoa"
         print(robot_brain)
         speak(robot_brain)
     elif "bai" in you:
         robot_brain = "Vâng"
         print("Robot: " + robot_brain)
         robot_mouth.say(robot_brain)
         robot_mouth.runAndWait()
         print(robot_brain)
         speak(robot_brain)
         break
     else: 
        robot_brain = "cảm ơn và xin chào"

     print("Robot: " + robot_brain)
     robot_mouth.say(robot_brain)
     robot_mouth.runAndWait()

