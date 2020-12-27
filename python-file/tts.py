# import pyttsx3
# import win32clipboard
# import win32com.client as wincl
# import keyboard
#
# speak = wincl.Dispatch("SAPI.SpVoice")
# speak.Speak("Hello World, I am rand, I am angry")
#
#
# def init():
#    print("init")
#
#    def start(text):
#       engine = pyttsx3.init()
#       # more code here but its just setting the volume and speech rate
#       engine.say(text, "txt")
#       engine.runAndWait()
#
#    def action():
#       win32clipboard.OpenClipboard()
#       data = win32clipboard.GetClipboardData()
#       win32clipboard.CloseClipboard()
#       start(data)
#
#    keyboard.add_hotkey("ctrl+alt", lambda: action())
#
#
# init()
#
#
# def onWord(name, location, length):
#    engine = pyttsx3.init()
#    print('word', name, location, length)
#    if keyboard.is_pressed("Alt"):
#       engine.stop()
#
#    engine.connect('started-word', onWord)
#
# onWord('word', 2,10)
# #
# #
# # def init():
# #    print("init")
# #
# #    def start(text):
# #       engine = pyttsx3.init()
# #       # more code here but its just setting the volume and speech rate
# #       engine.say("hello world! hello world! hello world! hello world! hello world!")
# #       engine.runAndWait()
# #
# #    def action():
# #       win32clipboard.OpenClipboard()
# #       data = win32clipboard.GetClipboardData()
# #       win32clipboard.CloseClipboard()
# #       start(data)
# #
# #    action()
# #
# #
# # init()
# #
# # tts_button = Button(self, text="listen", command=lambda: engine.endLoop())
# # tts_button.pack()
# #
# # def onWord():
# #    engine = pyttsx3.init()
# #
# #       engine.stop()
#
#
#
# import pyttsx3
#
# # def onWord(name, location, length):
# #     print('word', name, location, length)
# #     if location > 10:
# #         engine.stop()
# #
# # engine = pyttsx3.init()
# # rate = engine.getProperty('rate')
# # engine.setProperty('rate', 180)
# # engine.connect('dog', onWord('fox', 4, 0 ))
# # engine.say('The quick brown fox jumped over the lazy dog.')
# # engine.runAndWait()
# # #
# # #    engine.connect('started-word', onWord)
# engine = pyttsx3.init()
# def onStart(name):
#    print ('starting', name)
# def onWord(name, location, length):
#    print ('word', name, location, length)
# def onEnd(name, completed):
#    print ('finishing', name, completed)
#    if name == 'fox':
#       engine.say('What a lazy dog!', 'dog')
#    elif name == 'dog':
#       engine.endLoop()
#
# engine = pyttsx3.init()
# engine.connect('started-utterance', onStart)
# engine.connect('started-word', onWord)
# engine.connect('finished-utterance', onEnd)
# engine.say('The quick brown fox jumped over the lazy dog.', 'fox')
# engine.startLoop()
#
#
# # engine = pyttsx3.init()
# # engine.say('The quick brown fox jumped over the lazy dog.', 'fox')
# # engine.startLoop(False)
# # # engine.iterate() must be called inside externalLoop()
# # externalLoop()
# # engine.endLoop()
# #


# from win32com.client import Dispatch
# import tkinter as tk
#
# s = Dispatch("SAPI.SpVoice")
# def talk(x):
#    s.Speak(x.get("1.0", tk.END))
#
# root = tk.Tk()
# root.title("My Syntethic voice")
# root.geometry("300x200+200+300")
# label = tk.Label(root, text="ENTER TEXT BELOW")
# label.pack()
# text = tk.Text(root)
# if label =='stop':
#    tk.END
# else:
#    button = tk.Button(root, text="Click to speak", command=lambda : talk(text))
#    button.pack()
#
# text.pack()
# text.focus()
#
# root.mainloop()
import nltk
# import inflect
#
# p = inflect.engine()
# print(p.singular_noun('groups,'))
#
#
# a = 'groups'
# def singular(a):
#    for line in a:
#       line = line[0]
#       line = str(line)
#       stemmer = nltk.PorterStemmer()
#       line = stemmer.stem(line)
#       print (line)
#
#
# def stem(a):
#    for word in a:
#       for suffix in ['s']:
#          if word.endswith(suffix):
#             return word[:-len(suffix)]
#          print(word)
#
# singular(a)
# stem(a)


##################################################






