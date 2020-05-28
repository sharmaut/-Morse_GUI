import sys
from tkinter import *

import tkinter.font
from gpiozero import LED
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led1 = LED(20)

win = Tk()
word = StringVar()

win.geometry('450x450+500+300')
win.title('Morse Code')

def func1():
    try:
        mtext = word.get()
        if len(mtext) > 12:
            mlabel = Label(win, text = 'Entered word exceeds limit').pack()
        else:
            for x in mtext:
                for y in MORSE_CODE_DICTIONARY[x.lower()]:
                    if y == '.':
                        dot()
                        mlabel = Label(win, text = y).pack()
                    elif y == '-':
                        dash()
                        mlabel = Label(win, text = y).pack()
                    else:
                        time.sleep(0.2)    
                time.sleep(0.4)
                
    except KeyboardInterrupt:
        GPIO.cleanup()                
                
def dot():
        led1.on()
        time.sleep(0.2)
        led1.off()
        time.sleep(0.2)
def dash():
        led1.on()
        time.sleep(0.4)
        led1.off()
        time.sleep(0.4)
        
        
        
MORSE_CODE_DICTIONARY = {' ':' ', "'":'.----.', '(':'-.--.-', ')':'-.--.-', ',':'--..--', '-':'-....-', '.': '-.-.-.-', '/': '-..-.', 'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..'}
        
mbutton = Button(win, text = 'Execute', command = func1, fg = 'black').pack()
textEntry = Entry(win, textvariable = word).pack()



                
