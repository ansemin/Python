
from gtts import gTTS
from playsound import playsound


text='Welcome to the Microsoft AI School'

tts=gTTS(text=text, lang='en')
tts.save('hi.mp3')
playsound('hi.mp3')
