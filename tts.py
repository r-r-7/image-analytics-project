# import Google text-to-speech
from gtts import gTTS 
import os

# open text file
file = open("C:/Users/rahul/recognized.txt", "r").read().replace("\n", " ")

# set language as english
language = "en"

# convert text to speech
speech = gTTS(text = str(file), lang = language, slow = False)

# save speech in a mp3 file
speech.save("voice.mp3")
os.system("start voice.mp3")
