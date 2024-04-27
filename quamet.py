import speech_recognition as sr  
from gtts import gTTS 
import pygame
from pygame import mixer 
import time 
import requests 
import os  
#import time
import playsound   
from datetime import datetime
import wikipedia 
import requests
import json
import pyttsx3

now = datetime.now()


# initialize the recognizer
r=sr.Recognizer()
robot_brain = ""



def speak(text):
    tts = gTTS(text=text,lang='vi')
    filename='voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    pygame.mixer.init()
    pygame.mixer.music.load('voice.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
         time.sleep(1)
    os.remove(filename)
def tell_story():
    story = "Có một lần, ở một vương quốc xa xôi, có một chàng hoàng tử tài giỏi và một nàng công chúa xinh đẹp..."
    speak(story)
  
def get_weather_in_haiphong():
    api_key = "719971eee2ed82878b782010d7de5792"
    city = "Hải Phòng"  # Đặt tên thành phố là "Hải Phòng"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=vi"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        weather_info = f"""
        Thời tiết ở Hải Phòng hiện tại:
        - Trạng thái: {weather_description}
        - Nhiệt độ: {temperature} °C
        - Độ ẩm: {humidity} %
        """
        return weather_info
    else:
        return "Không thể lấy thông tin thời tiết."
while True:
    with sr.Microphone() as source:
        audio_data = r.record(source, duration=5)
        #print("Recognizing...")
        try:
                  text=r.recognize_google(audio_data,language="vi") 
        except:
                 text = ""
                 print(text)
        if text =="":
                 robot_brain = "Em nghe đây ạ"
                 print(robot_brain)
                 speak(robot_brain)
        elif "Xin chao" in text:
                 robot_brain = "Bạn muốn nói gì với tôi"
                 print(robot_brain)
                 speak(robot_brain)
        elif "ngày " in text:
                 robot_brain = now.strftime("%d/%m/%Y")
                 print(robot_brain)
                 speak(robot_brain)
        elif "nóng" in text:
                 robot_brain = "tao cũng nóng"
                 print(robot_brain)
                 speak(robot_brain)
        elif "kể chuyện" in text:
                 tell_story()
        elif "Mấy giờ rồi" in text:
                 robot_brain = now.strftime( "%H:%M:%S")
                 print(robot_brain)
                 speak(robot_brain)
        elif
        elif "thời tiết" in text:
                 speak("Bạn muốn hỏi thời tiết ở thành phố nào?")
                 city = input("Thành phố: Hải Phòng")
                 weather_info = get_weather_in_haiphong()
                 robot_brain = weather_info
        elif "tạm biệt" in text:
                 robot_brain= "Hẹn gặp lại bạn sau."   
                 print(robot_brain)
                 speak(robot_brain) 
                 break       
        else: 
                 robot_brain = "Bạn đang muốn nói gì với tôi"
                 print(robot_brain)
                 speak(robot_brain)


if __name__ == "__main__":
    main()
