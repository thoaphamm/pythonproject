import speech_recognition as sr
from gtts import gTTS
import pygame
import requests
import os
import playsound
from datetime import datetime
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
    r = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Chào bạn, bạn cần tôi giúp gì?")
            audio_data = r.listen(source)
            try:
                text = r.recognize_google(audio_data, language="vi-VN")
                print("Bạn nói:", text)

                if "Xin chào" in text:
                    robot_brain = "Chào bạn!"
                elif "ngày" in text:
                    robot_brain = now.strftime("%d/%m/%Y")
                elif "nóng" in text:
                    robot_brain = "Tôi cũng nóng!"
                elif "kể chuyện" in text:
                    tell_story()
                    continue  # Không cần tiếp tục xử lý sau khi kể chuyện xong
                elif "Mấy giờ rồi" in text:
                    robot_brain = now.strftime("%H:%M:%S")
                elif "thời tiết" in text:
                    speak("Bạn muốn hỏi thời tiết ở thành phố nào?")
                    audio_data = r.listen(source)
                    city = r.recognize_google(audio_data, language="vi-VN")
                    weather_info = get_weather_in_city(city)
                    if weather_info:
                        robot_brain = weather_info
                    else:
                        robot_brain = "Không thể lấy thông tin thời tiết cho thành phố này."
                elif "tạm biệt" in text:
                    robot_brain = "Hẹn gặp lại bạn sau!"
                    speak(robot_brain)
                    break  # Thoát khỏi vòng lặp while
                else:
                    robot_brain = "Xin lỗi, tôi không hiểu yêu cầu của bạn."

                print(robot_brain)
                speak(robot_brain)

            except sr.UnknownValueError:
                speak("Xin lỗi, tôi không nghe rõ. Bạn có thể nói lại không?")
            except sr.RequestError:
                speak("Xin lỗi, không thể kết nối đến máy chủ. Vui lòng thử lại sau.")

if __name__ == "__main__":
    main()
