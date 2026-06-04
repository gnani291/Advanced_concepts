#1. LOGGING
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program started")

#2. PATHLIB
from pathlib import Path

myfiles = ("data.csv", "acc.txt", "invite.docx")

print("\n--- File Path Details ---")
for filename in myfiles:
    p = Path("C:/Users/ai") / filename
    print("Path:", p)
    print("Anchor:", p.anchor)
    print("Drive:", p.drive)
    print("Stem:", p.stem)
    print("Suffix:", p.suffix)
    print("-" * 30)

# 3. OPEN WEBSITE
import webbrowser

logging.info("Opening YouTube in browser")
webbrowser.open("https://www.youtube.com")

#4. REQUESTS
import requests

print("\n--- HTTP Request ---")
response = requests.get("https://www.youtube.com")

if response.status_code == 200:
    print("YouTube request successful")
else:
    print("Error code:", response.status_code)

# 5. API KEY EXAMPLE (Weather API)
countrycode = "IN"
statecode = "AP"
cityname = "Bhimavaram"
apikey = "YOUR_API_KEY_HERE"

weather_url = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?q={cityname},{statecode},{countrycode}&appid={apikey}"
)

print("\n--- API Request ---")
api_response = requests.get(weather_url)

if api_response.status_code == 200:
    print(api_response.json())
else:
    print("API Error:", api_response.status_code)

# text to sppech using gtts
from gtts import gTTS
from IPython.display import Audio

text = "Hello world, how are you?"

tts = gTTS(text=text, lang="en")
tts.save("voice.mp3")

Audio("voice.mp3")




# 6. TEXT TO SPEECH
import pyttsx3

engine = pyttsx3.init()
engine.say("Hello, this is text to speech using Python")
engine.runAndWait()

#7.SPEECH TO TEXT (WHISPER)
import whisper

print("\n--- Speech Recognition ---")
model = whisper.load_model("base")
result = model.transcribe("hello.wav")  # use audio file
print("Recognized Text:", result["text"])

# 8.IMAGE TO TEXT (OCR)
import pytesseract
from PIL import Image

print("\n--- OCR Output ---")
img = Image.open("sample.png")  # local image file
ocr_text = pytesseract.image_to_string(img, lang="eng")
print(ocr_text)

#9.YOUTUBE VIDEO DOWNLOAD
import yt_dlp

print("\n--- Downloading YouTube Video ---")
video_url = "https://www.youtube.com/watch?v=VIDEO_ID"

ydl_opts = {
    "format": "best"
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

logging.info("Program completed successfully")
