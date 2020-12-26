from tkinter import *
import pygame
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
button1 = Button(root, bg="blue", fg="yellow", text='Play1', command= lambda: play('songs/1_In_His_Hands.mp3')).place(x=100
                                                                                                                      , y=420)
button2 = Button(root, text='Play2', command=lambda: play('songs/2_Good_Morning.mp3')).place(x=100, y=220)
button3 = Button(root, text='Play2', command=lambda: play('songs/8_Friends.mp3')).place(x=100, y=270)
button4 = Button(root, text='Play2', command=lambda: play('songs/533.mp3')).place(x=100, y=320)
button5 = Button(root, text='Play2', command=lambda: play('songs/796.mp3')).place(x=100, y=370)
button6 = Button(root, text='Play2', command=lambda: play('songs/2_Good_Morning.mp3')).place(x=450, y=220)
button7 = Button(root, text='Play2', command=lambda: play('songs/8_Friends.mp3')).place(x=450, y=270)
button8 = Button(root, text='Play2', command=lambda: play('songs/533.mp3')).place(x=450, y=320)
button9 = Button(root, text='Play2', command=lambda: play('songs/796.mp3')).place(x=450, y=370)
button0 = Button(root, text='Play2', command=lambda: play('songs/1_In_His_Hands.mp3')).place(x=450, y=420)
button13 = Button(root, text='stop', command=lambda: stop()).place(x=220, y=70)
button14 = Button(root, text='pause', command=lambda: pause()).place(x=300, y=70)
button15 = Button(root, text='unpause', command=lambda: unpause()).place(x=380, y=70)
root.geometry('600x610+400+100')
root.configure(bg="#afd")
root.mainloop()