import speech_recognition as sr
from tkinter import *
import tkinter as tk
def speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source, timeout = 2)
        print("Time over, Please wait few seconds")
        lol = r.recognize_google(audio_text)
    return str(lol)
root = tk.Tk()
b =  Button(root, text= "Start", command= speech)
b.pack()
    
root = mainloop()
