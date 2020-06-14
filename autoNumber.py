# autoNumber.py
# starts call and processes CALLINFO.txt
from time import sleep
from pynput.mouse import Button, Controller
import tkinter as tk
import threading, subprocess
from voiceGoogle import GoogleVoice

CALLINFO_ERROR = "CALLINFO.txt isn't configured properly"
CLICK_DELAY=1.5
DOUBLE_CLICK=2

#========================================================================
# DO NOT TOUCH ANYTHING ABOVE THIS LINE
#========================================================================

WIDTH_RES_MODIFIER=19/20 #change this to alter width the mouse will click
HEIGHT_RES_MODIFIER=1/16 #change this to alter height the mouse will click

#========================================================================
# DO NOT TOUCH ANYTHING BELOW THIS LINE
#========================================================================

# autoNumber(targetNumber, inMessage)
# instance of subprocess and saved info
# one constructor. autoInput throws Exception
class autoNumber:

    # Constructor to init our instance vars
    # to our saved input in CALLINFO.txt
    def __init__(self, targetNumber, message):
        self.targetNumber = targetNumber
        self.message = message

    # autoInputMessage()
    # calls the openFacetime with instance var
    # target number
    # throws
    #      Exception - Error Targeting FaceTime.app
    def autoInputMessage(self):
        GoogleVoice("Soccerback1@gmail.com","Emmadog99$$$", self.targetNumber, self.message)
        sleep(2) #wait until call is answered and then slight delay on top
    
# trys to get the input inside of the 
# CALLINFO which should only be written 
# to by bash script
if __name__ == "__main__":
    try:
        CALLINFO = open("CALLINFO.txt").readlines()
        PhoneString = CALLINFO[0]
        PhoneMessage = CALLINFO[1]
    except:
        print(CALLINFO_ERROR)

    autoNumber(PhoneString, PhoneMessage).autoInputMessage()
    