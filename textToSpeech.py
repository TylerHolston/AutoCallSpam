# textToSpeech.py
# need to brew install mpg123
from gtts import gTTS
from pygame import mixer, time
from os import getcwd
import subprocess
  
class textToSpeech:
    # Language in which you want to convert 
    language = 'en'

    def __init__(self, message):
        myobj = gTTS(text=message, lang=self.language, slow=False) 
        # Saving the converted audio in a mp3 file
        myobj.save("message.mp3") 
        # SAVE the current file
    
    def play(self):
        mixer.init()
        mixer.music.load(getcwd() + "\message.mp3")
        mixer.music.play()
        while mixer.music.get_busy(): 
            time.Clock().tick(10)