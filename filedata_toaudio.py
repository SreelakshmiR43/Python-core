from gtts import gTTS
import os
audio = open('text.txt','r', encoding='utf-8').read()
output = gTTS(text=audio,lang='hi',slow=False)
output.save('file_audio.mp3')
os.system('start file_audio.mp3')