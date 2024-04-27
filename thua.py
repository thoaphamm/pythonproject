import speech_recognition as sr
from gtts import gTTS
import pygame
import requests
import os
import playsound
from datetime import datetime

now = datetime.now()
r = sr.Recognizer()

def speak(text):
    tts = gTTS(text=text, lang='vi')
    filename = 'output.mp3'
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
    robot_brain = ""
    while True:
        with sr.Microphone() as source:
            print("Chào minh,bạn cần tôi giúp gì?")
            audio_data = r.record(source, duration=5)
            try:
                text = r.recognize_google(audio_data, language="vi")
            except sr.UnknownValueError:
                text = ""
            
            if text == "":
                robot_brain = "Bạn có cần hỗ trợ thêm không "
            elif "Chào minh" in text:
                robot_brain = "Em đây ạ,bạn cần tôi giúp gì ạ?"
            elif "ngày" in text:
                robot_brain = now.strftime("%d/%m/%Y")
            elif "nóng" in text:
                robot_brain = "Đủ để ướt áo ạ"
            elif "kể chuyện" in text:
                tell_story()
            elif "Mấy giờ rồi" in text:
                robot_brain = now.strftime("%H:%M:%S")  
            elif "đau đầu" in text:
                robot_brain = "Bạn nên dùng 1 viên paradol"
            elif"nóng đầu" in text:
                robot_brain = "Bạn nên kẹp nhiệt độ nếu quá mức cho phép bạn cần đến bác sĩ ngay"
            elif "thời tiết" in text:
                speak("Bạn muốn hỏi thời tiết ở thành phố nào?")
                city = input("Thành phố: Hải Phòng ")
                weather_info = get_weather_in_haiphong()
                robot_brain = weather_info
                speak(robot_brain)
            elif "tạm biệt" in text:
                robot_brain = "Hẹn gặp lại bạn sau"
                break
            else:
                robot_brain = "Chào minh,bạn cần giúp gì ạ"

            print(robot_brain)
            speak(robot_brain)

if __name__ == "__main__":
    main()
