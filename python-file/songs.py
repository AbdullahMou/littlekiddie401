from tkinter import *
import pygame
from PIL import Image, ImageTk
root = Tk()
pygame.mixer.init()
def play(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(-1)
def pause():
    pygame.mixer.music.pause()
def stop():
    pygame.mixer.music.stop()
def unpause():
    pygame.mixer.music.unpause()
c = Canvas(root)
c.pack(fill=BOTH, anchor='nw', expand=True)
img = ImageTk.PhotoImage(Image.open('..\\images\\Untitled design (1).jpg').resize((1540, 800), Image.ANTIALIAS))
c.background = img
bg = c.create_image(0, 0, anchor=NW, image=img)
c.create_text(780, 90, text='Songs ', font=("Comic Sans MS", 42))



c.create_text(200, 230, text='In His Hand ',font=("Comic Sans MS", 28))
button1 = ImageTk.PhotoImage(Image.open('..\\images\\play-button.png').resize((30, 30), Image.ANTIALIAS))
first_song = Button(c, image=button1, command=lambda: play('..\\songs\\1_In_His_Hands.mp3'))
first_song.place(x=340, y=220)
first_song.background = button1


c.create_text(200, 330, text='Good Morning ',font=("Comic Sans MS", 28))
button2 = ImageTk.PhotoImage(Image.open('..\\images\\play-button.png').resize((30, 30), Image.ANTIALIAS))
secound_song = Button(c, image=button2, command=lambda: play('..\\songs\\2_Good_Morning.mp3'))
secound_song.place(x=340, y=315)
secound_song.background = button2

c.create_text(200, 330, text='Friends ',font=("Comic Sans MS", 28))
button3 = Button(root, text='Friends',font=("Comic Sans MS", 20), bg = '#EF7D80',command=lambda: play('..\\songs\\8_Friends.mp3')).place(x=200, y=450)
button3 = ImageTk.PhotoImage(Image.open('..\\images\\play-button.png').resize((30, 30), Image.ANTIALIAS))
third_song = Button(c, image=button3, command=lambda: play('..\\songs\\8_Friends.mp3'))
third_song .place(x=340, y=315)
third_song .background = button2


# button4 = Button(root, text='Play2', command=lambda: play('..\\songs\\3_Body_Parts.mp3')).place(x=100, y=320)
# button5 = Button(root, text='Play2', command=lambda: play('..\\songs\\4_Clap_Your_Hands.mp3')).place(x=100, y=370)
# button6 = Button(root, text='Play2', command=lambda: play('..\\songs\\5_Funny_Long_Song.mp3')).place(x=450, y=220)
# button7 = Button(root, text='Play2', command=lambda: play('..\\songs\\6_Sing_for_Me.mp3')).place(x=450, y=270)
# button8 = Button(root, text='Play2', command=lambda: play('..\\songs\\7_Ready_to_Get_Washed.mp3')).place(x=450, y=320)
# button9 = Button(root, text='Play2', command=lambda: play('..\\songs\\bluebird-through-my-window.mp3')).place(x=450, y=370)
# button0 = Button(root, text='Play2', command=lambda: play('..\\songs\\dancing-rainbow-colors.mp3')).place(x=450, y=420)
button13 = Button(c, text='stop', command=lambda: stop()).place(x=480, y=750)
button14 = Button(c, text='pause', command=lambda: pause()).place(x=400, y=750)
button15 = Button(c, text='unpause', command=lambda: unpause())
button15.place(x=550, y=750)
root.geometry('1920x1080')
root.configure(bg="#afd")

root.mainloop()