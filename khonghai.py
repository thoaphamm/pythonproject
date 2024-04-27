import speech_recognition as sr
from gtts import gTTS
import pygame
import time
import requests
import os
import playsound
from datetime import datetime

now = datetime.now()
r = sr.Recognizer()

def speak(text):
    tts = gTTS(text=text, lang='vi')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def tell_story():
    story = "Có một lần, ở một vương quốc xa xôi, có một chàng hoàng tử tài giỏi và một nàng công chúa xinh đẹp..."
    speak(story)

def get_weather_in_haiphong():
    api_key = "719971eee2ed82878b782010d7de5792"
    city = "Hải Phòng"
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

def main():
    while True:
        with sr.Microphone() as source:
            print("Bạn có cần gì không?")
            audio_data = r.record(source, duration=5)
            
            try:
                text = r.recognize_google(audio_data, language="vi-VN")
                print("Bạn nói:", text)
            except sr.UnknownValueError:
                print("Xin lỗi, tôi không nghe rõ. Bạn có thể nói lại không?")
                text = ""

            if "Xin chào" in text:
                robot_brain = "Bạn muốn nói gì với tôi?"
            elif "ngày" in text:
                robot_brain = now.strftime("%d/%m/%Y")
            elif "nóng" in text:
                robot_brain = "Tôi cũng nóng"
            elif "kể chuyện" in text:
                tell_story()
                continue  # Bỏ qua các xử lý tiếp theo
            elif "Mấy giờ rồi" in text:
                robot_brain = now.strftime("%H:%M:%S")
            elif "thời tiết" in text:
                weather_info = get_weather_in_haiphong()
                robot_brain = weather_info
            elif "tạm biệt" in text:
                robot_brain = "Hẹn gặp lại bạn sau."
                speak(robot_brain)
                break
            els
