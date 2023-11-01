# Text to speech converter in python-Generating audio from text data
from gtts import gTTS
import os

speech = "Well, maybe i don't need your money.Wait,wait...,i said may be!"
output = gTTS(text=speech, lang='en', slow=False)
output.save('output.mp3')
os.system('start output.mp3')  # also we can convert it into mp4
