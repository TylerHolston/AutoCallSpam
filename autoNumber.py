# autoNumber.py
# starts call and processes CALLINFO.txt
from time import sleep
from pynput.mouse import Button, Controller
import tkinter as tk
from os import popen
from voiceGoogle import GoogleVoice

CALLINFO_ERROR = "CALLINFO.txt isn't configured properly"
    
# trys to get the input inside of the 
# CALLINFO which should only be written 
# to by bash script
if __name__ == "__main__":
    try:
        CALLINFO = open("CALLINFO.txt")
        lines = CALLINFO.readlines()
        PhoneString = lines[0].strip()
        PhoneMessage = lines[1].strip()
        EmailAddr = lines[2].strip()
        EmailPass = lines[3].strip()
        print(PhoneString + PhoneMessage + EmailAddr + EmailPass)
    except:
        print(CALLINFO_ERROR)

    GoogleVoice(EmailAddr, EmailPass, PhoneString, PhoneMessage)
    