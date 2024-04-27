import speech_recognition
from gtts import gTTS
import os
from datetime import date,datetime

while True:

    ai_brain = " "
    ai_ear = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as mic:
        print("AI: Nói đi bây...")
        audio = ai_ear.record(mic,duration = 5)

        print("\nAI:...")
    try:
        you = ai_ear.recognizer(audio, language = 'vi-VN')
         
        print("\nNguoi su dung: "  + you)
    except:
        ai_brain = "Tôi không hiểu bạn nói gi..."
        print("\nAI:  " + ai_brain)


    elif "giờ" in you:
        now = datetime.now()
        ai_brain = now.strftime("%H:%M:%S")
    elif "ngày " in you:
        today = date.today()
        ai_brain = today.strftime("%d/%m/%Y")
    elif "thời tiết" in you:
        ai_brain = "Tôi là máy móc nên chưa biết thời tiết nha"
    elif "Goodbye" in you:
        ai_brain = " Tạm biệt"
        print("\nAI: " + ai_brain)
        tts = gTTS(text = ai_brain, Lang = 'vi')
        tts.save("D:\\testcode\\youtube\\ai.mp3")
        os.system("D:\\testcode\\youtube\\ai.mp3")
        exit()
    else:
        ai_brain =" Cảm ơn Thoa"
        print("\nAI:  " + ai_brain) 
    
    print("\nAI: " + ai_brain)

    tts = gTTS(text = ai_brain, Lang = 'vi')
    tts.save("D:\\testcode\\youtube\\ai.mp3")
    os.system("D:\\testcode\\youtube\\ai.mp3")