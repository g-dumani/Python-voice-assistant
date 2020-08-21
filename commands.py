import subprocess
import os
from get_answer import Fetcher
import win32com.client as wincl
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")


class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm"]
        self.cancel = ["no", "negative", "negative soldier", "don't", "wait", "cancel"]

    def discover(self, text):
        if "what" in text and "name" in text:
            if "my" in text:
                self.respond("You haven't told me your name yet")
            else:
                self.respond("My name is Ar chill.  By the way Lay is CHUUTTIYA")
        if ".com" in text:
           app = text.split(" ",1)[-1]
           self.respond("Opening" + app)
           wb.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(text)
        else:
            f = Fetcher("https://www.google.ca/search?q=" + text)
            answer = f.lookup()
            self.respond(answer)





    def respond(self, response):
        speak.Speak(response)
        print(response)
        
