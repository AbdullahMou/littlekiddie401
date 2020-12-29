from tkinter import *
import pygame
pygame.init()
root = Tk()
root.title('Piano')
root.geometry('640x480')
root.configure(background = 'white')
abc = Frame(root,background = 'pink' )
abc.grid()
btnCs = (abc, )
if __name__ == '__main__':
    root.mainloop()