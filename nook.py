import speech_recognition as sr
from gtts import gTTS
import pygame
import requests
import os
import webbrowser as wb 
import pywhatkit
import time
import json
import sys
import re
import smtplib
import wikipedia
import playsound
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from pygame import mixer
from youtube_search import YoutubeSearch
now = datetime.now()
r = sr.Recognizer()
mixer.init()

wikipedia.set_lang('vi')
language = 'vi'
path = ChromeDriverManager().install()

def speak(text):
    if text:
         tts = gTTS(text=text, lang='vi')
         filename = 'output.mp3'
         tts.save(filename)
         # mixer.music.load(filename)
         # mixer.music.play()
         playsound.playsound(filename)
         os.remove(filename)
    else:
        print("Không có văn bản để phát âm.")    



def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("Minh không nghe rõ, ban có thể nói lại không ?")
    time.sleep(10)
    stop()
    return 0   


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end='')
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            return text
        except:
            print("...")
            return 0


def play_youtube():
    speak("Xin mời bạn chọn bài hát")
    time.sleep(3)
    my_song = get_text()
    while True:
        result = YoutubeSearch(my_song, max_results = 10).to_dict()
        if result:
            break;
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    wb.open(url)
    speak("Bài hát của bạn đã được mở, hãy thưởng thức nó!")

def tell_story():
     return "Có một lần, ở một vương quốc xa xôi, có một chàng hoàng tử tài giỏi và một nàng công chúa xinh đẹp...."

def read_news():
    speak("Bạn muốn đọc báo về gì?")
    
    # Lấy chủ đề từ người dùng
    topic = get_text()
    
    # Tạo tham số cho yêu cầu API
    params = {
        'apiKey': 'ae5af23daca6438e96af677df94889c6',
        'q': topic,
    }
    
    # Gửi yêu cầu GET đến API
    response = requests.get('http://newsapi.org/v2/top-headlines?', params=params)
    
    # Kiểm tra kết quả trả về từ API
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get('articles', [])
        
        if articles:
            speak("Đây là các tin tức liên quan:")
            for number, article in enumerate(articles[:3], start=1):
                title = article.get('title', 'Không có tiêu đề')
                description = article.get('description', 'Không có mô tả')
                url = article.get('url', '#')
                
                # Hiển thị thông tin tin tức
                news_info = f"Tin {number}: {title}. {description}."
                print(news_info)
                speak(news_info)
                
                # Mở trình duyệt web để xem tin tức chi tiết
                webbrowser.open(url)
        else:
            speak("Xin lỗi, không tìm thấy tin tức về chủ đề này.")
    else:
        speak("Xin lỗi, không thể kết nối đến dịch vụ tin tức.")

  

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
            print("------"+text)
            if text == "":
                robot_brain = "Bạn có cần hỗ trợ thêm không "
            elif "Chào minh" in text:
                robot_brain = "Em đây ạ,bạn cần tôi giúp gì ạ?"
            elif "ngày" in text:
                robot_brain = now.strftime("%d/%m/%Y")
            elif "nóng" in text:
                robot_brain = "Đủ để ướt áo ạ"
            elif "kể chuyện" in text:
                robot_brain =  tell_story()
            elif "Mấy giờ rồi" in text:
                robot_brain = now.strftime("%H:%M:%S")  
            elif "đau đầu" in text:
                robot_brain = "Bạn nên dùng 1 viên paradol"
            elif "bài hát" in text:
                 play_youtube()
            elif "đọc báo" in text:
                 read_news()
            elif"nóng đầu" in text:
                robot_brain = "Bạn nên kẹp nhiệt độ nếu quá mức cho phép bạn cần đến bác sĩ ngay"
            elif "tạm biệt" in text:
                robot_brain = "Hẹn gặp lại bạn sau"
                break
            elif "thời tiết" in text:
                speak("Bạn muốn hỏi thời tiết ở thành phố nào?")
                # city = input("Thành phố: Hải Phòng ")
                print("Thành phố: Hải Phòng ")
                weather_info = get_weather_in_haiphong()
                robot_brain = weather_info
            else:
                robot_brain = "Chào minh,bạn cần giúp gì ạ"

            print(robot_brain)
            speak(robot_brain)

if __name__ == "__main__":
    main()